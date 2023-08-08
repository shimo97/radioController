import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog, font

#CUSTOM COMPOUND WIDGETS
#widget composed of title label + combobox + button
class SelectFrame(Frame):
    def __init__(self,master,title,menuentries,buttonCallback,buttontext=""):
        Frame.__init__(self,master)
        
        self.title=Label(self, text=title)
        self.title.pack(side=LEFT, anchor=NW)
        self.selectedentry=StringVar()
        self.menu=ttk.Combobox(self,textvariable=self.selectedentry)
        self.menu['values']=menuentries
        self.menu['state']='readonly'
        self.menu.pack(side=LEFT, anchor=NW)
        self.butt=ttk.Button(self, text=buttontext, command=buttonCallback)
        self.butt.pack(side=LEFT, anchor=NW)
        
    def setButtonText(self,buttontext):
        self.butt.config(text=buttontext)
        
    def setMenuEntries(self, menuentries):
        self.menu['values']=menuentries
        
    def setSelectedEntry(self, selectedentry):
        self.selectedentry.set(selectedentry)
        
    def getSelectedEntry(self):
        return self.selectedentry.get()

#widget composed of title label + state label
#state label can be changed in text and color
class StatusFrame(Frame):
    def __init__(self,master,title,stateslist,statescolorlist):
        Frame.__init__(self,master)
        
        self.stateslist=stateslist
        self.statescolorlist=statescolorlist
        
        self.titlelabel=Label(self,text=title)
        self.titlelabel.pack(side=LEFT, anchor=NW)
        
        self.statelabel=Label(self,text=self.stateslist[0],fg=self.statescolorlist[0])
        self.statelabel.pack(side=LEFT, anchor=NW)

    def setStatusLabel(self, index):
        self.statelabel.config(text=self.stateslist[index],fg=self.statescolorlist[index])

#widget composed of title label + checkbox
class CheckFrame(Frame):
    def __init__(self,master,title,checktext,checkCallback):
        Frame.__init__(self,master)
        
        self.titlelabel=Label(self, text=title)
        self.titlelabel.pack(side=LEFT, anchor=NW)
        
        self.checkvariable=IntVar()
        self.checkbox=ttk.Checkbutton(self, text=checktext,variable=self.checkvariable,command=checkCallback)
        self.checkbox.pack(side=LEFT,anchor=W)
        
    def getCheckState(self):
        return self.checkvariable.get()
        
#widget composed of title label+ variable label (a bold label whose text can vary)
class DoubleLabel(Frame):
    def __init__(self,master,title,variabletext=""):
        Frame.__init__(self,master)
        
        self.titlelabel=Label(self, text=title)
        self.titlelabel.pack(side=LEFT, anchor=NW)

        defaultfont=font.nametofont("TkDefaultFont").copy()
        defaultfont.config(weight="bold")
        self.varlabel=Label(self, text=variabletext, font=defaultfont)
        self.varlabel.pack(side=RIGHT, anchor=NE,fill="x")

    def setVarText(self, vartext):
        self.varlabel.config(text=vartext)
        
#widget composed of title label+ entry widget
class TextInput(Frame):
    def traceCallback(self,*args):
        self.entryCallback()

    def __init__(self,master, title, entryCallback, starttext=""):
        Frame.__init__(self,master)
        
        self.title=title
        self.titlelabel=Label(self, text=title)
        self.titlelabel.pack(side=LEFT, anchor=NW)
        
        self.entryCallback=entryCallback
        self.textvar=tk.StringVar()
        self.textvar.trace_add("write", self.traceCallback)
        defaultfont=font.nametofont("TkDefaultFont").copy()
        defaultfont.config(weight="bold")
        self.textbox=Entry(self, textvariable=self.textvar, exportselection=0, justify=RIGHT, font=defaultfont, width=30)
        self.textbox.pack(side=LEFT, anchor=NW)
        self.setValid(1)
        
    def getText(self):
        return self.textvar.get()
        
    def setText(self,text):
        self.textvar.set(text)
        
    def setValid(self, value):
        if value==0:
            self.textbox.configure(bg="#f00")
        else:
            self.textbox.configure(bg="#fff")

#widget composed to a title label + label + a plus button + a minus button
#value can be set, this is used to input numbers (or others) 
class NumberBox(Frame):

    def __init__(self, master, title, minusCallback, plusCallback, startvalue=""):
        Frame.__init__(self,master)
        
        self.minusCallback=minusCallback
        self.plusCallback=plusCallback
        
        self.titlelabel=Label(self, text=title)
        self.titlelabel.pack(side=LEFT, anchor=NW)
        
        self.minusbutton=ttk.Button(self,text="-",command=self.minusCallback, width=2)
        self.minusbutton.pack(side=LEFT, anchor=NW, expand=0)
        
        defaultfont=font.nametofont("TkDefaultFont").copy()
        defaultfont.config(weight="bold")
        self.valuelabel=Label(self, text=startvalue, font=defaultfont)
        self.valuelabel.pack(side=LEFT, anchor=NW)
        
        self.plusbutton=ttk.Button(self,text="+",command=self.plusCallback, width=2)
        self.plusbutton.pack(side=LEFT, anchor=NW, expand=0)
        
    def setValue(self, value):
        self.valuelabel.config(text="{0}".format(value))

