from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Newuser import Newuser, Login


class main:     

        def __init__(self):
                self.GUI = Tk() 
                self.GUI.title('DCM')
                self.GUI.geometry("300x300")
                messagebox.showinfo(title= 'WELCOME USER!', message = 'Welcome to PaceYourself app, if you have an existing account please click login. If not please click NewUser!') 
                self.content = Frame(self.GUI)
                self.B0 = Label (self.content, text= 'PaceYourself Hub')
                self.BtnLogin = Button(self.content, text="LOGIN", command=self.login)
                self.BtnCancel = Button(self.content, text="CANCEL", command=self.cancel)
                self.BtnNewUser = Button(self.content, text='New User', command=self.Reg)
                self.content.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
                self.B0.grid(column=0, row=0, columnspan=2, sticky=W, pady=(0, 10))  
                self.BtnLogin.grid(column=0, row=1, columnspan=2, pady=(10, 5))
                self.BtnCancel.grid(column=0, row=3, columnspan=2, pady=5)
                self.BtnNewUser.grid(column=0, row=2, columnspan=2, pady=5)
                self.GUI.columnconfigure(0, weight=1)
                self.GUI.rowconfigure(0, weight=1)
                self.content.columnconfigure(0, weight=1)
                self.content.columnconfigure(1, weight=1)

        def login(self):
                self.log = Login()
                self.log.go()

        def cancel(self):
                self.GUI.destroy()
        
        def Reg(self):
                reg = Newuser()
                reg.go()

        def go(self):
                self.GUI.mainloop()

GUI = main()
GUI.go()