from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Database1 import Database
from Settings import Settings
import serialstuff

d1 = Database()
d1.maketable()

class Newuser:
    def __init__(self):
        self.newGUI2=Toplevel()
        self.Username = StringVar()
        self.Password = StringVar()
        self.newGUI2.geometry("300x300")
        self.content3 = Frame(self.newGUI2)
        self.NewNewb0 = Label (self.content3, text= 'PaceYourself New User Registration')
        self.NewNewb1 = Label (self.content3, text= 'Insert Login Name:')
        self.NewNewb2 = Label (self.content3, text= 'Insert Password: ')
        self.B111 = Entry(self.content3, textvariable=self.Username)
        self.B222 = Entry(self.content3, textvariable=self.Password)
        self.Btnregister1 = Button(self.content3, text="REGISTER", command=self.newcredentials)  
        self.BtnCancel11 = Button(self.content3, text="CANCEL", command=self.Cancel2)
        self.content3.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.NewNewb0.grid(column=0, row=0, columnspan=2, sticky=W, pady=(0, 10))  
        self.NewNewb1.grid(column=0, row=1, sticky=W)
        self.B111.grid(column=1, row=1, sticky=(W, E))
        self.NewNewb2.grid(column=0, row=2, sticky=W)
        self.B222.grid(column=1, row=2, sticky=(W, E))
        self.Btnregister1.grid(column=0, row=3, columnspan=2, pady=(10, 5))
        self.BtnCancel11.grid(column=0, row=4, columnspan=2, pady=5)
        self.newGUI2.columnconfigure(0, weight=1)
        self.newGUI2.rowconfigure(0, weight=1)
        self.content3.columnconfigure(0, weight=1)
        self.content3.columnconfigure(1, weight=1)
        self.newGUI2.mainloop()
    
    def newcredentials(self):          #code to check if the username used is unqiue or not, if it is user is registered. 
        username = self.Username.get()
        password = self.Password.get()
        data = (username,)
        result = d1.searchforusers(data)

        if (result != 0):
            datainput = (username, password)
            if (d1.addnewuser(datainput)):
                self.newGUI2.destroy()
                messagebox.showinfo("Success", "User has been registered") 
            else:
                messagebox.showinfo("Failed", "User limited reached - 10 users are already registered")
        else:
            messagebox.showinfo("Failed", "Username taken")
    
    def Cancel2(self):
        self.newGUI2.destroy()
    def go(self):
        self.newGUI2.mainloop()


class Login:
    def __init__(self):
        self.Username = StringVar()
        self.Password = StringVar()
        self.newGUI=Toplevel()
        self.newGUI.geometry("300x300")
        self.content2 = Frame(self.newGUI)
        self.Newb0 = Label (self.content2, text= 'PaceYourself LOGIN')
        self.Newb1 = Label (self.content2, text= 'Insert Login Name:')
        self.Newb2 = Label (self.content2, text= 'Insert Password: ')
        self.B11 = Entry(self.content2, textvariable=self.Username)
        self.B22 = Entry(self.content2, textvariable=self.Password)
        self.BtnLogin1 = Button(self.content2, text="LOGIN", command=self.validate)  #supposed to be verify 
        self.BtnCancel1 = Button(self.content2, text="CANCEL", command=self.cancel1)
        self.content2.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.Newb0.grid(column=0, row=0, columnspan=2, sticky=W, pady=(0, 10))  
        self.Newb1.grid(column=0, row=1, sticky=W)
        self.B11.grid(column=1, row=1, sticky=(W, E))
        self.Newb2.grid(column=0, row=2, sticky=W)
        self.B22.grid(column=1, row=2, sticky=(W, E))
        self.BtnLogin1.grid(column=0, row=3, columnspan=2, pady=(10, 5))
        self.BtnCancel1.grid(column=0, row=4, columnspan=2, pady=5)
        self.newGUI.columnconfigure(0, weight=1)
        self.newGUI.rowconfigure(0, weight=1)
        self.content2.columnconfigure(0, weight=1)
        self.content2.columnconfigure(1, weight=1)
        self.newGUI.mainloop()

    def validate(self):   #validation function to check if user logs in or not 
        username = self.Username.get()
        password = self.Password.get()
        data = (username,)
        datainput = (username, password,)

        try:
            if(d1.authy(data,datainput)):
                self.AOO = Settings(username)
                self.VOO = Settings(username)
                self.AAI = Settings(username)
                self.VVI = Settings(username)
                self.port1 = Settings(username)
                self.newGUI.destroy()
                messagebox.showinfo(title= 'Message', message = 'Succesfully Logged in') 
                self.newGUI3=Toplevel()
                self.newGUI3.geometry("400x300")
                self.content4 = Frame(self.newGUI3)
                self.NewNewNewb0 = Label (self.content4, text= 'PaceYourself Mode Selection')
                self.Btn1 = Button(self.content4, text="AOO", command=self.AOO.AOO)  
                self.Btn2 = Button(self.content4, text="VOO", command=self.VOO.VOO) 
                self.Btn3 = Button(self.content4, text="AAI", command=self.AAI.AAI) 
                self.Btn4 = Button(self.content4, text="VVI", command=self.VVI.VVI) 
              #  self.Btn5 = Button(self.content4, text="EGRAM", command= serialstuff.plot_egram()) 
                self.content4.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
                self.NewNewNewb0.grid(column=0, row=0, columnspan=2, sticky=W, pady=(0, 10))  
                self.Btn1.grid(column=0, row=3, columnspan=2, pady=(10, 5))
                self.Btn2.grid(column=0, row=4, columnspan=2, pady=5)
                self.Btn3.grid(column=0, row=5, columnspan=2, pady=5)
                self.Btn4.grid(column=0, row=6, columnspan=2, pady=5)
               # self.Btn4.grid(column=0, row=7, columnspan=2, pady=5)
                self.newGUI3.columnconfigure(0, weight=1)
                self.newGUI3.rowconfigure(0, weight=1)
                self.content4.columnconfigure(0, weight=1)
                self.content4.columnconfigure(1, weight=1)
                self.newGUI3.mainloop()

            else:           
                messagebox.showinfo(title= 'Message', message = 'Username OR password is wrong')
        
        except IndexError:
            messagebox.showinfo(title="Message", message= 'The Username or password is invalid, try again')

    def go(self):
            self.newGUI.mainloop()

    def cancel1(self):
            self.newGUI.destroy()

    def returnusername(self):
        return self.Username.get()
    

