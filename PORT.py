from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Database1 import Database
from serialstuff import Serialstuff
from Settings import Settings


s = Serialstuff()


class port:

    def connect(self):
        self.newGU=Toplevel()
        self.newGU.geometry("800x800")
        self.content12 = Frame(self.newGU)
        self.content12.grid(column=0, row=1, sticky=(N, S, E, W), padx=20, pady=20) 
        self.label = Label(self.content12, text = 'which port')
        self.label.grid(column=1,row=2,padx=20, pady=20, sticky="e")
        self.comPortSelect = ttk.Combobox(self.content12, values=s.serialList())
        self.comPortSelect.grid(column=1,row=3,padx=20, pady=20, sticky="e")
        self.btn= Button(self.content12, text="Connect", bg="white", command=self.Connectport)
        self.btn.grid (column=1,row=4,padx=20, pady=20, sticky="e")

        if s.State()[0]:
            self.disconLabel.place_forget()
            self.conlabel = ttk.Label(self.content12, text="Connected to Serial")
            self.label.grid(column=1,row=6,padx=20, pady=20, sticky="e")
            self.comPortSelect.set(s.State()[1])
        else:
            self.conlabel.place_forget()
            self.disconLabel = ttk.Label(self.content12, text="Disconnected from Serial")
            self.disconLabel.grid(column=1,row=7,padx=20, pady=20, sticky="e")
            self.comPortSelect.set(s.serialList()[0])

    def Connectport(self):
        val = Settings(self)
        s.Open(self.comPortSelect.get()[0:4])
        if s.State()[0]:
            self.disconLabel.place_forget()
            self.conlabel = ttk.Label(self.content12, text="Connected to Serial")
            self.label.grid(column=1,row=8,padx=20, pady=20, sticky="e")
            s.writeSettings(val.returnvals) 
        else:
            pass




