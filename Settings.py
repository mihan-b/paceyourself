from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Database1 import Database
import serialstuff

d1 = Database()

class Settings:
    def __init__(self, user):
        self.p_pacingMode = IntVar() 
        self.p_lowrateInterval = IntVar() 
        self.p_vPaceWidth = DoubleVar() 
        self.p_VRP = IntVar()
        self.p_aPaceWidth = DoubleVar() 
        self.p_ARP = IntVar() 
        self.p_BPM = IntVar()
        self.p_upperrateinterval = IntVar() 
        self.p_AV = IntVar()
        self.p_isAdaptive = IntVar()
        self.p_MSR = IntVar() 
        self.p_aPaceAmp = IntVar() 
        self.p_vPaceAmp = IntVar()  
        self.p_hysteresis = IntVar() 
        self.p_hystInterval = IntVar()  
        
        u1 = (user,)
        params = d1.searchforparameters(u1)
        self.Values = [item for i in params for item in i]
        self.Values.pop(0)

        IntVar.set(self.p_pacingMode, self.Values[0])
        IntVar.set(self.p_lowrateInterval, self.Values[1])
        IntVar.set(self.p_vPaceWidth, self.Values[2])
        IntVar.set(self.p_VRP, self.Values[3])
        DoubleVar.set(self.p_aPaceWidth, self.Values[4])
        IntVar.set(self.p_ARP , self.Values[5])
        DoubleVar.set(self.p_BPM, self.Values[6])
        IntVar.set(self.p_upperrateinterval, self.Values[7])
        IntVar.set(self.p_AV,self.Values[8])
        IntVar.set(self.p_isAdaptive,self.Values[9])
        IntVar.set(self.p_MSR,self.Values[10])
        DoubleVar.set(self.p_aPaceAmp,self.Values[11])
        DoubleVar.set(self.p_vPaceAmp,self.Values[12])
        IntVar.set(self.p_hysteresis,self.Values[13])
        IntVar.set(self.p_hystInterval,self.Values[14])
        
        
    def AOO(self):       #Code for AOO interface
        IntVar.set(self.p_pacingMode, 1)

        self.newGUI4=Toplevel()
        self.newGUI4.geometry("800x800")
        self.content5 = Frame(self.newGUI4)
        self.LAB1 = Label (self.content5, text= 'PaceYourself Mode AOO')
        self.Btn6 = Button(self.content5, text="Settings", command=self.AOOsettings) 

        self.lrllabel = Label(self.content5, text = "Lower Rate Limit")
        self.lrlval = Label(self.content5, text=self.p_lowrateInterval.get())
        self.lrlunit = Label(self.content5, text="ppm")

        self.urllabel = Label(self.content5, text = "Upper Rate Limit")
        self.urlval = Label(self.content5, text=self.p_upperrateinterval.get())
        self.urlunit = Label(self.content5, text="ppm")

        self.aamplabel= Label(self.content5, text = "Atrial Amplitude")
        self.aampval = Label(self.content5, text=self.p_aPaceAmp.get())
        self.aampunit = Label(self.content5, text="V")

        self.apwlabel = Label(self.content5, text = "Atrial Pulse-width")
        self.apwval = Label(self.content5, text=self.p_aPaceWidth.get())
        self.apwunit = Label(self.content5, text="ppm")

        self.vamplabel = Label(self.content5, text = "Ventricular Amplitude")
        self.vampval = Label(self.content5, text=self.p_vPaceAmp.get())
        self.vampunit = Label(self.content5, text="V")

        self.vpwlabel = Label(self.content5, text = "Ventricular Pulse-width")
        self.vpwval = Label(self.content5, text=self.p_vPaceWidth.get())
        self.vpwunit = Label(self.content5, text="ppm")

        self.bpmlabel = Label(self.content5, text = "Beats Per Minute")
        self.bpmval = Label(self.content5, text=self.p_BPM.get())
        self.bpmunit = Label(self.content5, text="bpm")

        self.AVlabel= Label(self.content5, text = "Atrial Event Delay")
        self.AVval = Label(self.content5, text=self.p_AV.get())
        self.AVunit = Label(self.content5, text="ms")

        self.msrlabel = Label(self.content5, text = "Max Sensor Rate")
        self.msrval = Label(self.content5, text=self.p_MSR.get())
        self.msrunit = Label(self.content5, text="ppm")

        self.hysteresislabel = Label(self.content5, text = "Hysteresis on/off")
        self.hysteresisval = Label(self.content5, text=self.p_hysteresis.get())

        self.hystintlabel = Label(self.content5, text = "Hysteresis Interval")
        self.hystintval = Label(self.content5, text=self.p_hystInterval.get())
        self.hystintunit = Label(self.content5, text="ppm")

        self.isadaplabel = Label(self.content5, text = "1 if rate adaptive is used (triggers AOOR)")
        self.isadapval = Label(self.content5, text=self.p_isAdaptive.get())


        self.content5.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.LAB1.grid(column=1, row=1, padx=20, pady=20, sticky="e")
        self.lrllabel.grid(column=1,row=2,padx=20, pady=20, sticky="e")
        self.lrlval.grid(column=2,row=2,padx=20, pady=20)
        self.lrlunit.grid(column=3,row=2,padx=20, pady=20, sticky="w")

        self.urllabel.grid(column=1,row=3,padx=20, pady=20, sticky="e")
        self.urlval.grid(column=2,row=3,padx=20, pady=20)
        self.urlunit.grid(column=3,row=3,padx=20, pady=20, sticky="w")

        self.aamplabel.grid(column=1,row=4,padx=20, pady=20, sticky="e")
        self.aampval.grid(column=2,row=4,padx=20, pady=20)
        self.aampunit.grid(column=3,row=4,padx=20, pady=20, sticky="w")

        self.apwlabel.grid(column=1,row=5,padx=20, pady=20, sticky="e")
        self.apwval.grid(column=2,row=5,padx=20, pady=20)
        self.apwunit.grid(column=3,row=5,padx=20, pady=20, sticky="w")

        self.vamplabel.grid(column=1,row=6,padx=20, pady=20, sticky="e")
        self.vampval.grid(column=2,row=6,padx=20, pady=20)
        self.vampunit.grid(column=3,row=6,padx=20, pady=20, sticky="w")

        self.vpwlabel.grid(column=1,row=7,padx=20, pady=20, sticky="e")
        self.vpwval.grid(column=2,row=7,padx=20, pady=20)
        self.vpwunit.grid(column=3,row=7,padx=20, pady=20, sticky="w")

        self.bpmlabel.grid(column=1,row=8,padx=20, pady=20, sticky="e")
        self.bpmval.grid(column=2,row=8,padx=20, pady=20)
        self.bpmunit.grid(column=3,row=8,padx=20, pady=20, sticky="w")

        self.AVlabel.grid(column=1,row=9,padx=20, pady=20, sticky="e")
        self.AVval.grid(column=2,row=9,padx=20, pady=20)
        self.AVunit.grid(column=3,row=9,padx=20, pady=20, sticky="w")

        self.msrlabel.grid(column=1,row=10,padx=20, pady=20, sticky="e")
        self.msrval.grid(column=2,row=10,padx=20, pady=20)
        self.msrunit.grid(column=3,row=10,padx=20, pady=20, sticky="w")

        self.hysteresislabel.grid(column=1,row=11,padx=20, pady=20, sticky="e")
        self.hysteresisval.grid(column=2,row=11,padx=20, pady=20)
        
        self.hystintlabel.grid(column=1,row=12,padx=20, pady=20, sticky="e")
        self.hystintval.grid(column=2,row=12,padx=20, pady=20)
        self.hystintunit.grid(column=3,row=12,padx=20, pady=20, sticky="w")

        self.Btn6.grid(column=3,row=13,padx=20, pady=20, sticky="w")

        self.content5.columnconfigure(4, weight=1)
        self.content5.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13), weight=1)
        self.newGUI4.mainloop()

    def VOO(self):   #Code for VOO interface
        IntVar.set(self.p_pacingMode, 0)
        self.newGUI5=Toplevel()
        self.newGUI5.geometry("800x800")
        self.content6 = Frame(self.newGUI5)
        self.LAB2 = Label (self.content6, text= 'PaceYourself Mode VOO')
        self.Btn7 = Button(self.content6, text="Settings", command=self.VOOsettings) 

        self.lrllabel1 = Label(self.content6, text = "Lower Rate Limit")
        self.lrlval1 = Label(self.content6, text=self.p_lowrateInterval.get())
        self.lrlunit1 = Label(self.content6, text="ppm")

        self.urllabel1 = Label(self.content6, text = "Upper Rate Limit")
        self.urlval1 = Label(self.content6, text=self.p_upperrateinterval.get())
        self.urlunit1 = Label(self.content6, text="ppm")

        self.vamplabel1 = Label(self.content6, text = "Ventricular Amplitude")
        self.vampval1 = Label(self.content6, text=self.p_vPaceAmp.get())
        self.vampunit1 = Label(self.content6, text="mV")

        self.vpwlabel1 = Label(self.content6, text = "Ventricular Pulse-width")
        self.vpwval1 = Label(self.content6, text=self.p_vPaceWidth.get())
        self.vpwunit1 = Label(self.content6, text="ppm")

        self.bpmlabel1 = Label(self.content6, text = "Beats Per Minute")
        self.bpmval1 = Label(self.content6, text=self.p_BPM.get())
        self.bpmunit1 = Label(self.content6, text="bpm")

        self.AVlabel1= Label(self.content6, text = "Atrial Event Delay")
        self.AVval1 = Label(self.content6, text=self.p_AV.get())
        self.AVunit1 = Label(self.content6, text="ms")

        self.msrlabel1 = Label(self.content6, text = "Max Sensor Rate")
        self.msrval1 = Label(self.content6, text=self.p_MSR.get())
        self.msrunit1 = Label(self.content6, text="ppm")

        self.hysteresislabel1 = Label(self.content6, text = "Hysteresis on/off")
        self.hysteresisval1 = Label(self.content6, text=self.p_hysteresis.get())

        self.hystintlabel1 = Label(self.content6, text = "Hysteresis Interval")
        self.hystintval1 = Label(self.content6, text=self.p_hystInterval.get())
        self.hystintunit1 = Label(self.content6, text="ppm")

        self.isadaplabel1 = Label(self.content6, text = " rate adaptive (1 triggers VOOR)")
        self.isadapval1 = Label(self.content6, text=self.p_isAdaptive.get())

        self.content6.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.LAB2.grid(column=1, row=1, padx=20, pady=20, sticky="e")
        self.lrllabel1.grid(column=1,row=2,padx=20, pady=20, sticky="e")
        self.lrlval1.grid(column=2,row=2,padx=20, pady=20)
        self.lrlunit1.grid(column=3,row=2,padx=20, pady=20, sticky="w")

        self.urllabel1.grid(column=1,row=3,padx=20, pady=20, sticky="e")
        self.urlval1.grid(column=2,row=3,padx=20, pady=20)
        self.urlunit1.grid(column=3,row=3,padx=20, pady=20, sticky="w")
    
        self.vamplabel1.grid(column=1,row=4,padx=20, pady=20, sticky="e")
        self.vampval1.grid(column=2,row=4,padx=20, pady=20)
        self.vampunit1.grid(column=3,row=4,padx=20, pady=20, sticky="w")

        self.vpwlabel1.grid(column=1,row=5,padx=20, pady=20, sticky="e")
        self.vpwval1.grid(column=2,row=5,padx=20, pady=20)
        self.vpwunit1.grid(column=3,row=5,padx=20, pady=20, sticky="w")

        self.Btn7.grid(column=3,row=12,padx=20, pady=20, sticky="w")

        self.bpmlabel1.grid(column=1,row=6,padx=20, pady=20, sticky="e")
        self.bpmval1.grid(column=2,row=6,padx=20, pady=20)
        self.bpmunit1.grid(column=3,row=6,padx=20, pady=20, sticky="w")

        self.AVlabel1.grid(column=1,row=7,padx=20, pady=20, sticky="e")
        self.AVval1.grid(column=2,row=7,padx=20, pady=20)
        self.AVunit1.grid(column=3,row=7,padx=20, pady=20, sticky="w")

        self.msrlabel1.grid(column=1,row=8,padx=20, pady=20, sticky="e")
        self.msrval1.grid(column=2,row=8,padx=20, pady=20)
        self.msrunit1.grid(column=3,row=8,padx=20, pady=20, sticky="w")

        self.hysteresislabel1.grid(column=1,row=9,padx=20, pady=20, sticky="e")
        self.hysteresisval1.grid(column=2,row=9,padx=20, pady=20)
        
        self.hystintlabel1.grid(column=1,row=10,padx=20, pady=20, sticky="e")
        self.hystintval1.grid(column=2,row=10,padx=20, pady=20)
        self.hystintunit1.grid(column=3,row=10,padx=20, pady=20, sticky="w")

        self.isadaplabel1.grid(column=1,row=11,padx=20, pady=20, sticky="e")
        self.isadapval1.grid(column=2,row=11,padx=20, pady=20)
        
        self.content6.columnconfigure(4, weight=1)
        self.content6.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=1)
        self.newGUI5.mainloop()

    def AAI(self):  #Code for AAI interface
        IntVar.set(self.p_pacingMode, 3)
        self.newGUI6=Toplevel()
        self.newGUI6.geometry("800x800")
        self.content7 = Frame(self.newGUI6)
        self.LAB3 = Label (self.content7, text= 'PaceYourself Mode AAI')
        self.Btn8 = Button(self.content7, text="Settings", command=self.AAIsettings) 

        self.lrllabel2 = Label(self.content7, text = "Lower Rate Limit")
        self.lrlval2 = Label(self.content7, text=self.p_lowrateInterval.get())
        self.lrlunit2 = Label(self.content7, text="ppm")

        self.urllabel2 = Label(self.content7, text = "Upper Rate Limit")
        self.urlval2 = Label(self.content7, text=self.p_upperrateinterval.get())
        self.urlunit2 = Label(self.content7, text="ppm")

        self.aamplabel2= Label(self.content7, text = "Atrial Amplitude")
        self.aampval2 = Label(self.content7, text=self.p_aPaceAmp.get())
        self.aampunit2 = Label(self.content7, text="V")

        self.apwlabel2 = Label(self.content7, text = "Atrial Pulse-width")
        self.apwval2 = Label(self.content7, text=self.p_aPaceWidth.get())
        self.apwunit2 = Label(self.content7, text="ppm")

        self.arplabel = Label(self.content7, text = "ARP")
        self.arpval = Label(self.content7, text=self.p_ARP.get())
        self.arpunit = Label(self.content7, text="ms")

        self.bpmlabel2= Label(self.content7, text = "Beats Per Minute")
        self.bpmval2 = Label(self.content7, text=self.p_BPM.get())
        self.bpmunit2 = Label(self.content7, text="bpm")

        self.AVlabel2= Label(self.content7, text = "Atrial Event Delay")
        self.AVval2 = Label(self.content7, text=self.p_AV.get())
        self.AVunit2 = Label(self.content7, text="ms")

        self.msrlabel2 = Label(self.content7, text = "Max Sensor Rate")
        self.msrval2 = Label(self.content7, text=self.p_MSR.get())
        self.msrunit2 = Label(self.content7, text="ppm")

        self.hysteresislabel2 = Label(self.content7, text = "Hysteresis on/off")
        self.hysteresisval2 = Label(self.content7, text=self.p_hysteresis.get())

        self.hystintlabel2 = Label(self.content7, text = "Hysteresis Interval")
        self.hystintval2 = Label(self.content7, text=self.p_hystInterval.get())
        self.hystintunit2 = Label(self.content7, text="ppm")

        self.isadaplabel2 = Label(self.content7, text = "rate adaptive (1 triggers AAIR)")
        self.isadapval2 = Label(self.content7, text=self.p_isAdaptive.get())

        self.content7.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.LAB3.grid(column=1, row=1, padx=20, pady=20, sticky="e")
        self.lrllabel2.grid(column=1,row=2,padx=20, pady=20, sticky="e")
        self.lrlval2.grid(column=2,row=2,padx=20, pady=20)
        self.lrlunit2.grid(column=3,row=2,padx=20, pady=20, sticky="w")

        self.urllabel2.grid(column=1,row=3,padx=20, pady=20, sticky="e")
        self.urlval2.grid(column=2,row=3,padx=20, pady=20)
        self.urlunit2.grid(column=3,row=3,padx=20, pady=20, sticky="w")

        self.aamplabel2.grid(column=1,row=4,padx=20, pady=20, sticky="e")
        self.aampval2.grid(column=2,row=4,padx=20, pady=20)
        self.aampunit2.grid(column=3,row=4,padx=20, pady=20, sticky="w")

        self.apwlabel2.grid(column=1,row=5,padx=20, pady=20, sticky="e")
        self.apwval2.grid(column=2,row=5,padx=20, pady=20)
        self.apwunit2.grid(column=3,row=5,padx=20, pady=20, sticky="w")
    
        self.arplabel.grid(column=1,row=6,padx=20, pady=20, sticky="e")
        self.arpval.grid(column=2,row=6,padx=20, pady=20)
        self.arpunit.grid(column=3,row=6,padx=20, pady=20, sticky="w")
        self.Btn8.grid(column=3,row=13,padx=20, pady=20, sticky="w")

        self.bpmlabel2.grid(column=1,row=7,padx=20, pady=20, sticky="e")
        self.bpmval2.grid(column=2,row=7,padx=20, pady=20)
        self.bpmunit2.grid(column=3,row=7,padx=20, pady=20, sticky="w")

        self.AVlabel2.grid(column=1,row=8,padx=20, pady=20, sticky="e")
        self.AVval2.grid(column=2,row=8,padx=20, pady=20)
        self.AVunit2.grid(column=3,row=8,padx=20, pady=20, sticky="w")

        self.msrlabel2.grid(column=1,row=9,padx=20, pady=20, sticky="e")
        self.msrval2.grid(column=2,row=9,padx=20, pady=20)
        self.msrunit2.grid(column=3,row=9,padx=20, pady=20, sticky="w")

        self.hysteresislabel2.grid(column=1,row=10,padx=20, pady=20, sticky="e")
        self.hysteresisval2.grid(column=2,row=10,padx=20, pady=20)
        
        self.hystintlabel2.grid(column=1,row=11,padx=20, pady=20, sticky="e")
        self.hystintval2.grid(column=2,row=11,padx=20, pady=20)
        self.hystintunit2.grid(column=3,row=11,padx=20, pady=20, sticky="w")

        self.isadaplabel2.grid(column=1,row=12,padx=20, pady=20, sticky="e")
        self.isadapval2.grid(column=2,row=12,padx=20, pady=20)

        self.content7.columnconfigure(4, weight=1)
        self.content7.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13), weight=1)
        self.newGUI6.mainloop()

    def VVI(self):  #Code for VVI interface
        IntVar.set(self.p_pacingMode, 2)
        self.mode = 4
        self.newGUI7=Toplevel()
        self.newGUI7.geometry("800x800")
        self.content8 = Frame(self.newGUI7)
        self.LAB4 = Label (self.content8, text= 'PaceYourself Mode VVI')
        self.Btn9 = Button(self.content8, text="Settings", command=self.VVIsettings)

        self.lrllabel3 = Label(self.content8, text = "Lower Rate Limit")
        self.lrlval3 = Label(self.content8, text=self.p_lowrateInterval.get())
        self.lrlunit3 = Label(self.content8, text="ppm")

        self.urllabel3 = Label(self.content8, text = "Upper Rate Limit")
        self.urlval3 = Label(self.content8, text=self.p_upperrateinterval.get())
        self.urlunit3 = Label(self.content8, text="ppm")

        self.vamplabel3 = Label(self.content8, text = "Ventricular Amplitude")
        self.vampval3 = Label(self.content8, text=self.p_vPaceAmp.get())
        self.vampunit3 = Label(self.content8, text="V")

        self.vpwlabel3 = Label(self.content8, text = "Ventricular Pulse-width")
        self.vpwval3 = Label(self.content8, text=self.p_vPaceWidth.get())
        self.vpwunit3 = Label(self.content8, text="ppm")

        self.vrplabel = Label(self.content8, text = "VRP")
        self.vrpval = Label(self.content8, text=self.p_VRP.get())
        self.vrpunit = Label(self.content8, text="ms")


        self.bpmlabel3= Label(self.content8, text = "Beats Per Minute")
        self.bpmval3 = Label(self.content8, text=self.p_BPM.get())
        self.bpmunit3 = Label(self.content8, text="bpm")

        self.AVlabel3= Label(self.content8, text = "Atrial Event Delay")
        self.AVval3 = Label(self.content8, text=self.p_AV.get())
        self.AVunit3 = Label(self.content8, text="ms")

        self.msrlabel3 = Label(self.content8, text = "Max Sensor Rate")
        self.msrval3 = Label(self.content8, text=self.p_MSR.get())
        self.msrunit3 = Label(self.content8, text="ppm")

        self.hysteresislabel3 = Label(self.content8, text = "Hysteresis on/off")
        self.hysteresisval3 = Label(self.content8, text=self.p_hysteresis.get())

        self.hystintlabel3 = Label(self.content8, text = "Hysteresis Interval")
        self.hystintval3 = Label(self.content8, text=self.p_hystInterval.get())
        self.hystintunit3 = Label(self.content8, text="ppm")

        self.isadaplabel3 = Label(self.content8, text = "1 if rate adaptive is used (triggers VVIR)")
        self.isadapval3= Label(self.content8, text=self.p_isAdaptive.get())

        self.content8.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.LAB4.grid(column=1, row=1, padx=20, pady=20, sticky="e")
        self.lrllabel3.grid(column=1,row=2,padx=20, pady=20, sticky="e")
        self.lrlval3.grid(column=2,row=2,padx=20, pady=20)
        self.lrlunit3.grid(column=3,row=2,padx=20, pady=20, sticky="w")

        self.urllabel3.grid(column=1,row=3,padx=20, pady=20, sticky="e")
        self.urlval3.grid(column=2,row=3,padx=20, pady=20)
        self.urlunit3.grid(column=3,row=3,padx=20, pady=20, sticky="w")
    
        self.vamplabel3.grid(column=1,row=4,padx=20, pady=20, sticky="e")
        self.vampval3.grid(column=2,row=4,padx=20, pady=20)
        self.vampunit3.grid(column=3,row=4,padx=20, pady=20, sticky="w")

        self.vpwlabel3.grid(column=1,row=5,padx=20, pady=20, sticky="e")
        self.vpwval3.grid(column=2,row=5,padx=20, pady=20)
        self.vpwunit3.grid(column=3,row=5,padx=20, pady=20, sticky="w")

        self.vrplabel.grid(column=1,row=6,padx=20, pady=20, sticky="e")
        self.vrpval.grid(column=2,row=6,padx=20, pady=20)
        self.vrpunit.grid(column=3,row=6,padx=20, pady=20, sticky="w")
        self.Btn9.grid(column=3,row=13,padx=20, pady=20, sticky="w")

        self.bpmlabel3.grid(column=1,row=7,padx=20, pady=20, sticky="e")
        self.bpmval3.grid(column=2,row=7,padx=20, pady=20)
        self.bpmunit3.grid(column=3,row=7,padx=20, pady=20, sticky="w")

        self.AVlabel3.grid(column=1,row=8,padx=20, pady=20, sticky="e")
        self.AVval3.grid(column=2,row=8,padx=20, pady=20)
        self.AVunit3.grid(column=3,row=8,padx=20, pady=20, sticky="w")

        self.msrlabel3.grid(column=1,row=9,padx=20, pady=20, sticky="e")
        self.msrval3.grid(column=2,row=9,padx=20, pady=20)
        self.msrunit3.grid(column=3,row=9,padx=20, pady=20, sticky="w")

        self.hysteresislabel3.grid(column=1,row=10,padx=20, pady=20, sticky="e")
        self.hysteresisval3.grid(column=2,row=10,padx=20, pady=20)
        
        self.hystintlabel3.grid(column=1,row=11,padx=20, pady=20, sticky="e")
        self.hystintval3.grid(column=2,row=11,padx=20, pady=20)
        self.hystintunit3.grid(column=3,row=11,padx=20, pady=20, sticky="w")
        
        self.isadaplabel3.grid(column=1,row=12,padx=20, pady=20, sticky="e")
        self.isadapval3.grid(column=2,row=12,padx=20, pady=20)
        
        self.content8.columnconfigure(4, weight=1)
        self.content8.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13), weight=1)
        self.newGUI7.mainloop()

    def VOOsettings(self):
        self.newGUI5.destroy()
        self.newGUI9=Toplevel()
        self.newGUI9.geometry("800x800")
        self.content10 = Frame(self.newGUI9)
        self.content10.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.settingslab1 = Label (self.content10, text= 'Settings')
        self.settingslab1.grid(column=2, row=1, padx=20, pady=20)
        self.lrllabs1 = Label(self.content10, text = 'lower rate limit')
        self.lrllabs1.grid(column=1, row=2, padx=20, pady=20)
        self.lrlinput1 = Entry(self.content10, textvariable=self.p_lowrateInterval, justify=CENTER)
        self.lrlinput1.grid(column=2, row=2, padx=20, pady=20)
        self.lrlinput1.config(validate="key", validatecommand="%P")
        self.Urllabs1 = Label(self.content10, text = 'Upper rate limit')
        self.Urllabs1.grid(column=1, row=3, padx=20, pady=20)
        self.urlinput1 = Entry(self.content10, textvariable=self.p_upperrateinterval, justify=CENTER)
        self.urlinput1.grid(column=2, row=3, padx=20, pady=20)
        self.urlinput1.config(validate="key", validatecommand="%P")
        self.vamplabs1 = Label(self.content10, text = 'Ventricular Amplitude')
        self.vamplabs1.grid(column=1, row=4, padx=20, pady=20)
        self.vampinput1 = Entry(self.content10, textvariable=self.p_vPaceAmp , justify=CENTER)
        self.vampinput1.grid(column=2, row=4, padx=20, pady=20)
        self.vampinput1.config(validate="key", validatecommand="%P")
        self.vpwlabs1 = Label(self.content10, text = 'Ventricular Pulse-width')
        self.vpwlabs1.grid(column=1, row=5, padx=20, pady=20)
        self.vpwinput1 = Entry(self.content10, textvariable=self.p_aPaceWidth, justify=CENTER)
        self.vpwinput1.grid(column=2, row=5, padx=20, pady=20)
        self.vpwinput1.config(validate="key", validatecommand="%P")
       
        self.bpmlabs1 = Label(self.content10, text = "Beats Per Minute" )
        self.bpmlabs1.grid(column=1, row=6, padx=20, pady=20)
        self.bpminput1 = Entry(self.content10, textvariable=self.p_BPM, justify=CENTER)
        self.bpminput1.grid(column=2, row=6, padx=20, pady=20)
        self.bpminput1.config(validate="key", validatecommand="%P")

        self.AVlabs1 = Label(self.content10, text = "AV Delay" )
        self.AVlabs1.grid(column=1, row=7, padx=20, pady=20)
        self.AVinput1 = Entry(self.content10, textvariable=self.p_AV, justify=CENTER)
        self.AVinput1.grid(column=2, row=7, padx=20, pady=20)
        self.AVinput1.config(validate="key", validatecommand="%P")


        self.msrlabs1 = Label(self.content10, text = "Max Sensor Rate" )
        self.msrlabs1.grid(column=1, row=8, padx=20, pady=20)
        self.msrinput1 = Entry(self.content10, textvariable=self.p_MSR, justify=CENTER)
        self.msrinput1.grid(column=2, row=8, padx=20, pady=20)
        self.msrinput1.config(validate="key", validatecommand="%P")

        self.hysteresislabs1 = Label(self.content10, text = "Hysteresis" )
        self.hysteresislabs1.grid(column=1, row=9, padx=20, pady=20)
        self.hysteresisinput1 = Entry(self.content10, textvariable=self.p_hysteresis, justify=CENTER)
        self.hysteresisinput1.grid(column=2, row=9, padx=20, pady=20)
        self.hysteresisinput1.config(validate="key", validatecommand="%P")

        self.hystintlabs1 = Label(self.content10, text = "Hysteresis Interval" )
        self.hystintlabs1.grid(column=1, row=10, padx=20, pady=20)
        self.hystintinput1 = Entry(self.content10, textvariable=self.p_hystInterval, justify=CENTER)
        self.hystintinput1.grid(column=2, row=10, padx=20, pady=20)
        self.hystintinput1.config(validate="key", validatecommand="%P")

        self.isadaplabs1 = Label(self.content10, text = "Adaptive" )
        self.isadaplabs1.grid(column=1, row=11, padx=20, pady=20)
        self.isadapinput1 = Entry(self.content10, textvariable=self.p_isAdaptive, justify=CENTER)
        self.isadapinput1.grid(column=2, row=11, padx=20, pady=20)
        self.isadapinput1.config(validate="key", validatecommand="%P")
    

        self.confirmbutton1 = Button(self.content10, text = "Confirm", command=self.confirminputs1)
        self.confirmbutton1.grid(column=5,row=12,sticky="w", padx=5, pady=5)
        self.cancelbutton1 = Button(self.content10, text = "Cancel", command=self.newGUI9.destroy)
        self.cancelbutton1.grid(column=5,row=13,sticky="w", padx=5, pady=5)
        self.newGUI9.mainloop()

    def AOOsettings(self):
        self.newGUI4.destroy()
        self.newGUI8=Toplevel()
        self.newGUI8.geometry("800x800")
        self.content9 = Frame(self.newGUI8)
        self.content9.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.settingslab = Label (self.content9, text= 'Settings')
        self.settingslab.grid(column=2, row=1, padx=20, pady=20)
        self.lrllabs = Label(self.content9, text = 'lower rate limit')
        self.lrllabs.grid(column=1, row=2, padx=20, pady=20)
        self.lrlinput = Entry(self.content9, textvariable=self.p_lowrateInterval, justify=CENTER)
        self.lrlinput.grid(column=2, row=2, padx=20, pady=20)
        self.lrlinput.config(validate="key", validatecommand="%P")
        self.Urllabs = Label(self.content9, text = 'Upper rate limit')
        self.Urllabs.grid(column=1, row=3, padx=20, pady=20)
        self.urlinput = Entry(self.content9, textvariable=self.p_upperrateinterval, justify=CENTER)
        self.urlinput.grid(column=2, row=3, padx=20, pady=20)
        self.urlinput.config(validate="key", validatecommand="%P")
        self.aamplabs = Label(self.content9, text = 'Atrial Amplitude')
        self.aamplabs.grid(column=1, row=4, padx=20, pady=20)
        self.aampinput = Entry(self.content9, textvariable=self.p_aPaceAmp, justify=CENTER)
        self.aampinput.grid(column=2, row=4, padx=20, pady=20)
        self.aampinput.config(validate="key", validatecommand="%P")
        self.apwlabs = Label(self.content9, text = 'Atrial Pulse-width')
        self.apwlabs.grid(column=1, row=5, padx=20, pady=20)
        self.apwinput = Entry(self.content9, textvariable=self.p_aPaceWidth, justify=CENTER)
        self.apwinput.grid(column=2, row=5, padx=20, pady=20)
        self.apwinput.config(validate="key", validatecommand="%P")

        self.bpmlabs = Label(self.content9, text = "Beats Per Minute" )
        self.bpmlabs.grid(column=1, row=6, padx=20, pady=20)
        self.bpminput = Entry(self.content9, textvariable=self.p_BPM, justify=CENTER)
        self.bpminput.grid(column=2, row=6, padx=20, pady=20)
        self.bpminput.config(validate="key", validatecommand="%P")

        self.AVlabs = Label(self.content9, text = "AV Delay" )
        self.AVlabs.grid(column=1, row=7, padx=20, pady=20)
        self.AVinput = Entry(self.content9, textvariable=self.p_AV, justify=CENTER)
        self.AVinput.grid(column=2, row=7, padx=20, pady=20)
        self.AVinput.config(validate="key", validatecommand="%P")


        self.msrlabs = Label(self.content9, text = "Max Sensor Rate" )
        self.msrlabs.grid(column=1, row=8, padx=20, pady=20)
        self.msrinput = Entry(self.content9, textvariable=self.p_MSR, justify=CENTER)
        self.msrinput.grid(column=2, row=8, padx=20, pady=20)
        self.msrinput.config(validate="key", validatecommand="%P")

        self.hysteresislabs = Label(self.content9, text = "Hysteresis" )
        self.hysteresislabs.grid(column=1, row=9, padx=20, pady=20)
        self.hysteresisinput = Entry(self.content9, textvariable=self.p_hysteresis, justify=CENTER)
        self.hysteresisinput.grid(column=2, row=9, padx=20, pady=20)
        self.hysteresisinput.config(validate="key", validatecommand="%P")

        self.hystintlabs = Label(self.content9, text = "Hysteresis Interval" )
        self.hystintlabs.grid(column=1, row=10, padx=20, pady=20)
        self.hystintinput = Entry(self.content9, textvariable=self.p_hystInterval, justify=CENTER)
        self.hystintinput.grid(column=2, row=10, padx=20, pady=20)
        self.hystintinput.config(validate="key", validatecommand="%P")

        self.isadaplabs = Label(self.content9, text = "Adaptive" )
        self.isadaplabs.grid(column=1, row=11, padx=20, pady=20)
        self.isadapinput = Entry(self.content9, textvariable=self.p_isAdaptive, justify=CENTER)
        self.isadapinput.grid(column=2, row=11, padx=20, pady=20)
        self.isadapinput.config(validate="key", validatecommand="%P")

        self.confirmbutton = Button(self.content9, text = "Confirm", command=self.confirminputs)
        self.confirmbutton.grid(column=5,row=12,sticky="w", padx=5, pady=5)
        self.cancelbutton = Button(self.content9, text = "Cancel", command=self.newGUI8.destroy)
        self.cancelbutton.grid(column=5,row=13,sticky="w", padx=5, pady=5)
        self.newGUI8.mainloop()

    def AAIsettings(self):
        self.newGUI6.destroy()
        self.newGUI10=Toplevel()
        self.newGUI10.geometry("800x800")
        self.content11 = Frame(self.newGUI10)
        self.content11.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.settingslab2 = Label (self.content11, text= 'Settings')
        self.settingslab2.grid(column=2, row=1, padx=20, pady=20)
        self.lrllabs2 = Label(self.content11, text = 'lower rate limit')
        self.lrllabs2.grid(column=1, row=2, padx=20, pady=20)
        self.lrlinput2 = Entry(self.content11, textvariable=self.p_lowrateInterval, justify=CENTER)
        self.lrlinput2.grid(column=2, row=2, padx=20, pady=20)
        self.lrlinput2.config(validate="key", validatecommand="%P")
        self.Urllabs2 = Label(self.content11, text = 'Upper rate limit')
        self.Urllabs2.grid(column=1, row=3, padx=20, pady=20)
        self.urlinput2 = Entry(self.content11, textvariable=self.p_upperrateinterval, justify=CENTER)
        self.urlinput2.grid(column=2, row=3, padx=20, pady=20)
        self.urlinput2.config(validate="key", validatecommand="%P")\
        
        self.aamplabs = Label(self.content11, text = 'Atrial Amplitude')
        self.aamplabs.grid(column=1, row=4, padx=20, pady=20)
        self.aampinput = Entry(self.content11, textvariable=self.p_aPaceAmp, justify=CENTER)
        self.aampinput.grid(column=2, row=4, padx=20, pady=20)
        self.aampinput.config(validate="key", validatecommand="%P")

        self.apwlabs2 = Label(self.content11, text = 'Atrial Pulse-width')
        self.apwlabs2.grid(column=1, row=5, padx=20, pady=20)
        self.apwinput2 = Entry(self.content11, textvariable=self.p_aPaceWidth, justify=CENTER)
        self.apwinput2.grid(column=2, row=5, padx=20, pady=20)
        self.apwinput2.config(validate="key", validatecommand="%P")

        self.arplabs2 = Label(self.content11, text = 'Atrial Refractory Period')
        self.arplabs2.grid(column=1, row=6, padx=20, pady=20)
        self.arpinput2 = Entry(self.content11, textvariable=self.p_ARP, justify=CENTER)
        self.arpinput2.grid(column=2, row=6, padx=20, pady=20)
        self.arpinput2.config(validate="key", validatecommand="%P")

        self.bpmlabs2 = Label(self.content11, text = "Beats Per Minute" )
        self.bpmlabs2.grid(column=1, row=7, padx=20, pady=20)
        self.bpminput2 = Entry(self.content11, textvariable=self.p_BPM, justify=CENTER)
        self.bpminput2.grid(column=2, row=7, padx=20, pady=20)
        self.bpminput2.config(validate="key", validatecommand="%P")

        self.AVlabs2 = Label(self.content11, text = "AV Delay" )
        self.AVlabs2.grid(column=1, row=8, padx=20, pady=20)
        self.AVinput2 = Entry(self.content11, textvariable=self.p_AV, justify=CENTER)
        self.AVinput2.grid(column=2, row=8, padx=20, pady=20)
        self.AVinput2.config(validate="key", validatecommand="%P")


        self.msrlabs2 = Label(self.content11, text = "Max Sensor Rate" )
        self.msrlabs2.grid(column=1, row=9, padx=20, pady=20)
        self.msrinput2 = Entry(self.content11, textvariable=self.p_MSR, justify=CENTER)
        self.msrinput2.grid(column=2, row=9, padx=20, pady=20)
        self.msrinput2.config(validate="key", validatecommand="%P")

        self.hysteresislabs2 = Label(self.content11, text = "Hysteresis" )
        self.hysteresislabs2.grid(column=1, row=10, padx=20, pady=20)
        self.hysteresisinput2 = Entry(self.content11, textvariable=self.p_hysteresis, justify=CENTER)
        self.hysteresisinput2.grid(column=2, row=10, padx=20, pady=20)
        self.hysteresisinput2.config(validate="key", validatecommand="%P")

        self.hystintlabs2 = Label(self.content11, text = "Hysteresis Interval" )
        self.hystintlabs2.grid(column=1, row=11, padx=20, pady=20)
        self.hystintinput2 = Entry(self.content11, textvariable=self.p_hystInterval, justify=CENTER)
        self.hystintinput2.grid(column=2, row=11, padx=20, pady=20)
        self.hystintinput2.config(validate="key", validatecommand="%P")

        self.isadaplabs2 = Label(self.content11, text = "Adaptive" )
        self.isadaplabs2.grid(column=1, row=12, padx=20, pady=20)
        self.isadapinput2 = Entry(self.content11, textvariable=self.p_isAdaptive, justify=CENTER)
        self.isadapinput2.grid(column=2, row=12, padx=20, pady=20)
        self.isadapinput2.config(validate="key", validatecommand="%P")

        self.confirmbutton2 = Button(self.content11, text = "Confirm", command=self.confirminputs2)
        self.confirmbutton2.grid(column=5,row=13,sticky="w", padx=5, pady=5)
        self.cancelbutton2 = Button(self.content11, text = "Cancel", command=self.newGUI10.destroy)
        self.cancelbutton2.grid(column=5,row=14,sticky="w", padx=5, pady=5)
        self.newGUI10.mainloop()

    def VVIsettings(self):
        self.newGUI7.destroy()
        self.newGUI11=Toplevel()
        self.newGUI11.geometry("800x800")
        self.content12 = Frame(self.newGUI11)
        self.content12.grid(column=0, row=0, sticky=(N, S, E, W), padx=20, pady=20) 
        self.settingslab3 = Label (self.content12, text= 'Settings')
        self.settingslab3.grid(column=2, row=1, padx=20, pady=20)
        self.lrllabs3 = Label(self.content12, text = 'lower rate limit')
        self.lrllabs3.grid(column=1, row=2, padx=20, pady=20)
        self.lrlinput3 = Entry(self.content12, textvariable=self.p_lowrateInterval, justify=CENTER)
        self.lrlinput3.grid(column=2, row=2, padx=20, pady=20)
        self.lrlinput3.config(validate="key", validatecommand="%P")
        self.Urllabs3 = Label(self.content12, text = 'Upper rate limit')
        self.Urllabs3.grid(column=1, row=3, padx=20, pady=20)
        self.urlinput3 = Entry(self.content12, textvariable=self.p_upperrateinterval, justify=CENTER)
        self.urlinput3.grid(column=2, row=3, padx=20, pady=20)
        self.urlinput3.config(validate="key", validatecommand="%P")

        self.vamplabs3 = Label(self.content12, text = 'Ventricular Amplitude')
        self.vamplabs3.grid(column=1, row=4, padx=20, pady=20)
        self.vampinput3 = Entry(self.content12, textvariable=self.p_vPaceAmp , justify=CENTER)
        self.vampinput3.grid(column=2, row=4, padx=20, pady=20)
        self.vampinput3.config(validate="key", validatecommand="%P")
        self.vpwlabs3 = Label(self.content12, text = 'Ventricular Pulse-width')
        self.vpwlabs3.grid(column=1, row=5, padx=20, pady=20)
        self.vpwinput3 = Entry(self.content12, textvariable=self.p_aPaceWidth, justify=CENTER)
        self.vpwinput3.grid(column=2, row=5, padx=20, pady=20)
        self.vpwinput3.config(validate="key", validatecommand="%P")

        self.vrplabs3 = Label(self.content12, text = 'Ventricular Refractory Period')
        self.vrplabs3.grid(column=1, row=6, padx=20, pady=20)
        self.vrpinput3 = Entry(self.content12, textvariable=self.p_VRP, justify=CENTER)
        self.vrpinput3.grid(column=2, row=6, padx=20, pady=20)
        self.vrpinput3.config(validate="key", validatecommand="%P")

        self.bpmlabs3 = Label(self.content12, text = "Beats Per Minute" )
        self.bpmlabs3.grid(column=1, row=7, padx=20, pady=20)
        self.bpminput3 = Entry(self.content12, textvariable=self.p_BPM, justify=CENTER)
        self.bpminput3.grid(column=2, row=7, padx=20, pady=20)
        self.bpminput3.config(validate="key", validatecommand="%P")

        self.AVlabs3 = Label(self.content12, text = "AV Delay" )
        self.AVlabs3.grid(column=1, row=8, padx=20, pady=20)
        self.AVinput3 = Entry(self.content12, textvariable=self.p_AV, justify=CENTER)
        self.AVinput3.grid(column=2, row=8, padx=20, pady=20)
        self.AVinput3.config(validate="key", validatecommand="%P")

        self.msrlabs3 = Label(self.content12, text = "Max Sensor Rate" )
        self.msrlabs3.grid(column=1, row=9, padx=20, pady=20)
        self.msrinput3 = Entry(self.content12, textvariable=self.p_MSR, justify=CENTER)
        self.msrinput3.grid(column=2, row=9, padx=20, pady=20)
        self.msrinput3.config(validate="key", validatecommand="%P")

        self.hysteresislabs3 = Label(self.content12, text = "Hysteresis" )
        self.hysteresislabs3.grid(column=1, row=10, padx=20, pady=20)
        self.hysteresisinput3 = Entry(self.content12, textvariable=self.p_hysteresis, justify=CENTER)
        self.hysteresisinput3.grid(column=2, row=10, padx=20, pady=20)
        self.hysteresisinput3.config(validate="key", validatecommand="%P")

        self.hystintlabs3 = Label(self.content12, text = "Hysteresis Interval" )
        self.hystintlabs3.grid(column=1, row=11, padx=20, pady=20)
        self.hystintinput3 = Entry(self.content12, textvariable=self.p_hystInterval, justify=CENTER)
        self.hystintinput3.grid(column=2, row=11, padx=20, pady=20)
        self.hystintinput3.config(validate="key", validatecommand="%P")

        self.isadaplabs3 = Label(self.content12, text = "Adaptive" )
        self.isadaplabs3.grid(column=1, row=12, padx=20, pady=20)
        self.isadapinput3 = Entry(self.content12, textvariable=self.p_isAdaptive, justify=CENTER)
        self.isadapinput3.grid(column=2, row=12, padx=20, pady=20)
        self.isadapinput3.config(validate="key", validatecommand="%P")

        self.confirmbutton3 = Button(self.content12, text = "Confirm", command=self.confirminputs3)
        self.confirmbutton3.grid(column=5,row=13,sticky="w", padx=5, pady=5)
        self.cancelbutton3 = Button(self.content12, text = "Cancel", command=self.newGUI11.destroy)
        self.cancelbutton3.grid(column=5,row=13,sticky="w", padx=5, pady=5)
        self.newGUI11.mainloop()

    def confirminputs(self):
        wrong= False
        if ((self.p_lowrateInterval.get() >= 30) and (self.p_lowrateInterval.get() <= 175))!=1:
            wrong = True
            messagebox.showerror("ERROR, Lower Rate Limit must be between 175-1200")
        if ((self.p_upperrateinterval.get() >= 50) and (self.p_upperrateinterval.get() <= 175))!=1:
            wrong = True
            messagebox.showerror("ERROR, Upper Rate Limit must be between 175-2000")
        if ((self.p_aPaceAmp.get() < 500) or (self.p_aPaceAmp.get() > 5000)):
            wrong = True
            messagebox.showerror("ERROR, Atrial Amplitude must be between 500 and 5000 or 0 for off")
        if ((self.p_aPaceWidth.get() >= 0.05) and (self.p_aPaceWidth.get() <= 1.9))!=1:
            wrong = True
            messagebox.showerror("ERROR, Atrial Pulse Width must be between 0.05 and 1.9")
        if ((self.p_BPM.get() >= 0) and (self.p_BPM.get() <= 255))!=1:
            wrong = True
            messagebox.showerror("ERROR, Beats per minute must be between 0 and 255")
        if ((self.p_AV.get() >= 70) and (self.p_AV.get() <=300))!=1:
            wrong = True
            messagebox.showerror("ERROR, AV must be between 70 and 300")
        if ((self.p_MSR.get() >= 0 ) and (self.p_MSR.get() <= 175))!=1:
            wrong = True
            messagebox.showerror("ERROR, MSR must be between 0 and 175")
        if ((self.p_hysteresis.get() not in [0,1])):
            wrong = True
            messagebox.showerror("ERROR, hysteresis must be 0 or 1")

        if (self.p_hystInterval.get() >= 0 and (self.p_hystInterval.get() <=200))!=1:
            wrong = True
            messagebox.showerror("ERROR, hysteresis interval must be between 0 and 200")

        if (self.p_isAdaptive.get() not in [0,1]):
            wrong = True
            messagebox.showerror("ERROR, Adaptive must be 0 or 1")

        if wrong:
            pass

        else:
            self.newGUI8.update()
            self.updatevals()
            self.AOO()

    def confirminputs1(self):
            wrong= False
            if ((self.p_lowrateInterval.get() >= 30) and (self.p_lowrateInterval.get() <= 175))!=1:
                wrong = True
                messagebox.showerror("ERROR, Lower Rate Limit must be between 175-2000")
            if ((self.p_upperrateinterval.get() >= 50) and (self.p_upperrateinterval.get() <= 175))!=1:
                wrong= True
                messagebox.showerror("ERROR, Upper Rate Limit must be between 175-1200")
            if ((self.p_vPaceAmp.get() < 500) or (self.p_vPaceAmp.get() > 5000)):
                wrong = True
                messagebox.showerror("ERROR, Ventricular Ampltiude must be between 500 a 5000 or 0 for off")
            if ((self.p_vPaceWidth.get() >= 0.05) and (self.p_vPaceWidth.get() <= 1.9))!=1:
                wrong = True
                messagebox.showerror("ERROR, Ventricular Pulse Width must be between 0.05 and 1.9")
            if ((self.p_BPM.get() >= 0) and (self.p_BPM.get() <= 255))!=1:
                wrong = True
                messagebox.showerror("ERROR, Beats per minute must be between 0 and 255")
            if ((self.p_AV.get() >= 70) and (self.p_AV.get() <=300))!=1:
                wrong = True
                messagebox.showerror("ERROR, AV must be between 70 and 300")
            if ((self.p_MSR.get() >= 0 ) and (self.p_MSR.get() <= 175))!=1:
                wrong = True
                messagebox.showerror("ERROR, MSR must be between 0 and 175")
            if ((self.p_hysteresis.get() not in [0,1])):
                wrong = True
                messagebox.showerror("ERROR, hysteresis must be 0 or 1")
            if (self.p_hystInterval.get() >= 0 and (self.p_hystInterval.get() <=200))!=1:
                wrong = True
                messagebox.showerror("ERROR, hysteresis interval must be between 0 and 200")
            if ((self.p_isAdaptive.get() not in [0,1])):
                wrong = True
                messagebox.showerror("ERROR, Adaptive must be 0 or 1")

            if wrong:
                # Do nothing on invalid input to force user to correct error
                    pass
            else:
                self.newGUI9.update()
                self.updatevals()
                self.VOO()

    def confirminputs2(self):
            wrong= False
            if ((self.p_lowrateInterval.get() >=30) and (self.p_lowrateInterval.get() <= 175))!=1:
                wrong= True
                messagebox.showerror("ERROR, Lower Rate Limit must be between 175-1200")
            if ((self.p_upperrateinterval.get() >= 50) and (self.p_upperrateinterval.get() <= 175))!=1:
                wrong = True
                messagebox.showerror("ERROR, Upper Rate Limit must be between 175-2000")
            if ((self.p_aPaceAmp.get() < 500) or (self.p_aPaceAmp.get() >5000)):
                wrong = True
                messagebox.showerror("ERROR, Atrial Amplitude must be between 500 and 5000 or 0 for off")
            if ((self.p_aPaceWidth.get() >= 0.05) and (self.p_aPaceWidth.get() <= 1.9))!=1:
                wrong = True
                messagebox.showerror("ERROR, Atrial Pulse Width must be between 0.05 and 1.9")
            if ((self.p_ARP.get() >= 150) and (self.p_ARP.get() <= 500))!=1:
                wrong= True
                messagebox.showerror("ERROR, ARP must be between 150 and 500")
            if ((self.p_BPM.get() >= 0) and (self.p_BPM.get() <= 255))!=1:
                wrong = True
                messagebox.showerror("ERROR, Beats per minute must be between 0 and 255")
            if ((self.p_AV.get() >= 70) and (self.p_AV.get() <=300))!=1:
                wrong = True
                messagebox.showerror("ERROR, AV must be between 70 and 300")
            if ((self.p_MSR.get() >= 0 ) and (self.p_MSR.get() <= 175))!=1:
                wrong = True
                messagebox.showerror("ERROR, MSR must be between 0 and 175")
            if (self.p_hysteresis.get() not in [0,1]):
                wrong = True
                messagebox.showerror("ERROR, hysteresis must be 0 or 1")
            if (self.p_hystInterval.get() >= 0 and (self.p_hystInterval.get() <=200))!=1:
                wrong = True
                messagebox.showerror("ERROR, hysteresis interval must be between 0 and 200")
            if (self.p_isAdaptive.get() not in [0,1]):
                wrong = True
                messagebox.showerror("ERROR, Adaptive must be 0 or 1")
            if wrong:
                # Do nothing on invalid input to force user to correct error
                pass
            else:
                self.newGUI10.update()
                self.updatevals()
                self.AAI()

    def confirminputs3(self):
            wrong= False
            if ((self.p_lowrateInterval.get() >= 30) and (self.p_lowrateInterval.get() <= 175))!=1:
                wrong = True
                messagebox.showerror("ERROR, Lower Rate Limit must be between 175-1200")
            if ((self.p_upperrateinterval.get() >= 30) and (self.p_upperrateinterval.get() <= 175))!=1:
                wrong = True
                messagebox.showerror("ERROR, Upper Rate Limit must be between 175-2000")
            if ((self.p_vPaceAmp.get() < 500) or (self.p_vPaceAmp.get() > 5000)):
                wrong = True
                messagebox.showerror("ERROR, Ventricular Ampltiude must be between 500 and 5000 or 0 for off")
            if ((self.p_vPaceWidth.get() >= 0.05) and (self.p_vPaceWidth.get() < 1.9))!=1:
                wrong = True
                messagebox.showerror("ERROR, Ventricular Pulse Width must be between 0.05 and 1.9")
            if ((self.p_VRP.get() >= 150) and (self.p_VRP.get() <= 500))!=1:
                wrong = True
                messagebox.showerror("ERROR, VRP must be between 150 and 500")
            
            if ((self.p_BPM.get() >= 0) and (self.p_BPM.get() <= 255))!=1:
                wrong = True
                messagebox.showerror("ERROR, Beats per minute must be between 0 and 255")
            if ((self.p_AV.get() >= 70) and (self.p_AV.get() <=300))!=1:
                wrong = True
                messagebox.showerror("ERROR, AV must be between 70 and 300")
            if ((self.p_MSR.get() >= 0 ) and (self.p_MSR.get() <= 175))!=1:
                wrong = True
                messagebox.showerror("ERROR, MSR must be between 0 and 175")
            if (self.p_hysteresis.get() not in [0,1]):
                wrong = True
                messagebox.showerror("ERROR, hysteresis must be 0 or 1")
            if (self.p_hystInterval.get() >= 0 and (self.p_hystInterval.get() <=200))!=1:
                wrong = True
                messagebox.showerror("ERROR, hysteresis interval must be between 0 and 200")
            if (self.p_isAdaptive.get() not in [0,1]):
                wrong = True
                messagebox.showerror("ERROR, Adaptive must be 0 or 1")
            if wrong:
                # Do nothing on invalid input to force user to correct error
                pass
            else:
                self.newGUI11.update()
                self.updatevals()
                self.VVI()

    def updatevals(self):
        self.NEWVALUES =  [self.p_pacingMode.get(), self.p_lowrateInterval.get(), self.p_vPaceWidth.get(), self.p_VRP.get(), self.p_aPaceWidth.get(),
                           self.p_ARP.get(), self.p_BPM.get(), self.p_upperrateinterval.get(), self.p_AV.get(), self.p_isAdaptive.get(), self.p_MSR.get(),
                           self.p_aPaceAmp.get(), self.p_vPaceAmp.get(), self.p_hysteresis.get(), self.p_hystInterval.get()]
        d1.updatetheParameters(tuple(self.NEWVALUES))
        serialstuff.writeSettings(self.p_pacingMode.get(), self.p_lowrateInterval.get(), self.p_vPaceWidth.get(), self.p_VRP.get(), self.p_aPaceWidth.get(),
                           self.p_ARP.get(), self.p_BPM.get(), self.p_upperrateinterval.get(), self.p_AV.get(), self.p_isAdaptive.get(), self.p_MSR.get(),
                           self.p_aPaceAmp.get(), self.p_vPaceAmp.get(), self.p_hysteresis.get(), self.p_hystInterval.get())

    def returnvals(self):
        return   [self.p_pacingMode.get(), self.p_lowrateInterval.get(), self.p_vPaceWidth.get(), self.p_VRP.get(), self.p_aPaceWidth.get(),
                           self.p_ARP.get(), self.p_BPM.get(), self.p_upperrateinterval.get(), self.p_AV.get(), self.p_isAdaptive.get(), self.p_MSR.get(),
                           self.p_aPaceAmp.get(), self.p_vPaceAmp.get(), self.p_hysteresis.get(), self.p_hystInterval.get()]



