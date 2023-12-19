import sqlite3

#database class 

class Database:          

    def  __init__(self):  #making a connection to a sqlite3 db file, creates one if not there, and then create a cursor
        self.access = sqlite3.connect("data6.db")
        self.cur = self.access.cursor()

    def maketable(self):     #creating a table for username and password and another table for the parameters 
        maketab= """CREATE TABLE IF NOT EXISTS tab(
            id Integer PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """   
        self.cur.execute(maketab)
        self.access.commit()

        parametertable= """CREATE TABLE IF NOT EXISTS parametertb(
            id Integer PRIMARY KEY AUTOINCREMENT,
            p_pacingMode DEFAULT 0,
            p_lowrateInterval DEFAULT 60,
            p_vPaceWidth DEFAULT 1.00,
            p_VRP DEFAULT 320,
            p_aPaceWidth DEFAULT 1.00,
            p_ARP DEFAULT 250,
            p_BPM DEFAULT 70,
            p_upperrateinterval DEFAULT 120,
            p_AV DEFAULT 150,
            p_isAdaptive Default 0,
            p_MSR Default 175,
            p_aPaceAmp Default 3500,
            p_vPaceAmp Default 3500,
            p_hysteresis Default 0,
            p_hystInterval Default 100
        );
        """
        self.cur.execute(parametertable)
        self.access.commit()

    def addnewuser(self, datainput):      #code to add a new User by getting the rownumbers and seeing if less than 10. If so, we insert username and password into db file
        rownum_query = "SELECT Count() FROM tab"
        self.cur.execute(rownum_query)
        rownum = self.cur.fetchone()[0] 
        
        if(rownum<10):
           insert_query = """INSERT INTO tab (username, password) VALUES (?, ?);"""
           self.cur.execute(insert_query, datainput)
           self.access.commit()
           insert_param = "INSERT INTO parametertb DEFAULT VALUES;"
           self.cur.execute(insert_param)
           self.access.commit()
           return 1
        return 0 
    
    def authy (self,data,datainput):        #code to aunthenticate whether username is present in file 
        auth = "SELECT * FROM tab WHERE username = (?);"
        self.cur.execute(auth, data)
        row = self.cur.fetchall()
        if row [0][1] == datainput[0]:
            return row[0][2] == datainput[1]

    def searchforusers(self, data):            #code to search if the user is in the file, if yes returns 1 
        search_user_query = "SELECT * FROM tab WHERE username = (?);"
        self.cur.execute(search_user_query, data)
        rows = self.cur.fetchall()
        if rows == []:
            return 1
        return 0

    def searchforparameters(self, data):           #code to search for the parameters 
        search_user = "SELECT * from tab WHERE username = (?);"
        self.cur.execute(search_user, data)
        self.rowid = self.cur.fetchall()

        search_params = "SELECT * from parametertb WHERE id = (?);"
        self.cur.execute(search_params, (self.rowid[0][0],))
        params = self.cur.fetchall()
        return params
        
    def updatetheParameters(self, params):
        newtable = params + (self.rowid[0][0],)
        update = """UPDATE parametertb
            SET p_pacingMode=?,
                p_lowrateInterval=?,
                p_vPaceWidth=?,
                p_VRP=?,
                p_aPaceWidth=?,
                p_ARP=?,
                p_BPM=?,
                p_upperrateinterval=?,
                p_AV=?,
                p_isAdaptive=?,
                p_MSR=?,
                p_aPaceAmp=?,
                p_vPaceAmp=?,
                p_hysteresis=?,
                p_hystInterval=?
            WHERE id = ?
        ;
        """
        self.cur.execute(update,newtable)
        self.access.commit()

