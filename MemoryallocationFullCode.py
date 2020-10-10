import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import tkinter
from tkinter import *
from tkinter import ttk
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,QMainWindow
import sys
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
import matplotlib.pyplot as plt

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

import matplotlib.animation as animation
from matplotlib import style

#import importlib

#moduleName = input('first-fit')
#importlib.import_module(moduleName)

#############sho8l sika ##########################



'''
def AddAnotherProcess(TotalMemSize,HoleStarting, HoleSize, Mem, Start, Size):
    HoleStarting.clear()
    HoleSize.clear()
    for i in range(len(Mem)):
        if Mem[i] == "hole":
            HoleStarting.append(Start[i])
            HoleSize.append(Size[i])

    ProcessName = input()

    SegmentsNameString = input()
    Z = SegmentsNameString.split(',')
    SegmentName = []
    for i in range(len(Z)):
        SegmentName.append(ProcessName + " " + Z[i])

    SegmentSizeString = input()
    B = SegmentSizeString.split(',')
    SegmentSize = []
    for i in range(len(B)):
        SegmentSize.append(int(B[i]))
    Mem, Start, Size, token = FirstFit(TotalMemSize, HoleStarting, HoleSize, ProcessName, SegmentName, SegmentSize, Mem,
                                       Start, Size)
    return Mem, Start, Size, token


'''


def DeAllocate(Mem, Start, Size,ProcessName):
    for i in range(len(Mem)):
        Temp = Mem[i].split(" ")

        if Temp[0] == ProcessName:
            Mem[i] = "hole"
    i = 0
    while i < (len(Mem)-1):
        if Mem[i] == "hole" and Mem[i + 1] == "hole":
            Size[i] = Size[i] + Size[i + 1]
            del Size[i + 1]
            del Start[i + 1]
            del Mem[i + 1]
            i -= 1
        i += 1


    HoleStarting.clear()
    HoleSize.clear()
    for i in range(len(Mem)):
        if Mem[i] == "hole":
            HoleStarting.append(Start[i])
            HoleSize.append(Size[i])

    return Mem, Start, Size


'''
def InputFirstFit ():

    TotalMemSize=int(input())

    HolesStartingString=input()
    X=HolesStartingString.split(',')
    HoleStarting = []
    for i in range (len(X)):
        HoleStarting.append(int(X[i]))

    HolesSizeString=input()
    Y=HolesSizeString.split(',')
    HoleSize=[]
    for i in range (len(Y)):
        HoleSize.append(int(Y[i]))

    ProcessName=input()

    NoOfSegments=int(input())

    SegmentsNameString=input()
    Z=SegmentsNameString.split(',')
    SegmentName=[]
    for i in range (len(Z)):
        SegmentName.append(ProcessName+" "+Z[i])



    SegmentSizeString=input()
    B=SegmentSizeString.split(',')
    SegmentSize=[]
    for i in range (len(B)):
        SegmentSize.append(int(B[i]))



    return TotalMemSize,HoleStarting,HoleSize,ProcessName,SegmentName,SegmentSize,Mem,Start,Size
'''
def FirstFit (TotalMemSize,HoleStarting,HoleSize,ProcessName,SegmentName,SegmentSize,Mem,Start,Size):
    j=0
    token=0
    SegmentStart = []

################-------To Shamy Code----------------#####

    if Mem==[]:
        for i in range(len(HoleSize)):
            Mem.append("hole")
            Start.append(HoleStarting[i])
            Size.append(HoleSize[i])
        if Start[0]>0:
            Mem.insert(0,"PreAllocated")
            Start.insert(0,0)
            Size.insert(0,Start[1])
        counter=0
        while counter <len(Mem)-1:
            if Mem[counter] == "hole"  and Start[counter+1] > (Start[counter]+Size[counter]):
                Mem.insert(counter+1,"PreAllocated")
                Start.insert(counter+1,(Start[counter]+Size[counter]))
                Size.insert(counter+1,Start[counter+2]-Start[counter+1])
            counter += 1
        if Mem[len(Mem)-1]=="hole" and (Start[len(Mem)-1]+Size[len(Mem)-1])<TotalMemSize:
            Mem.append("PreAllocated")
            Start.append((Start[len(Mem)-2]+Size[len(Mem)-2]))
            Size.append((TotalMemSize-Start[len(Mem)-1]))


###########-------------------------------#####


    for i in range(len(SegmentName)):
        while j < (len(HoleStarting)):
            if SegmentSize[i] <= HoleSize[j]:
                for k in range(len(Size)):
                    if Mem[k]=="hole" and Size[k] >= SegmentSize[i]:
                        break
                Mem.insert(k,SegmentName[i])
                SegmentStart.append(HoleStarting[j])
                Start.insert(k,int(SegmentStart[i]))
                Size.insert(k,int(SegmentSize[i]))
                Size[k+1]=HoleSize[j]-SegmentSize[i]
                Start[k+1]= HoleStarting[j]+SegmentSize[i]
                HoleSize[j] = HoleSize[j]-SegmentSize[i]
                HoleStarting[j] = HoleStarting[j]+SegmentSize[i]
                if HoleSize[j] == 0:
                    del HoleSize[j]
                    del HoleStarting[j]
                    del Size[k+1]
                    del Start[k+1]
                    del Mem[k+1]
                   # NoOfDeletedHoles+=1
                j=0
                break                           # 3achan a5rog lw 7sl fit mydawwarch 3la holes tany

            elif j == len(HoleSize)-1:      #kda el segment not fit any hole
                 token= -1
            j += 1

    return Mem, Start, Size,token



def bestfit (TotalMemSize,HoleStarting,HoleSize,ProcessName,SegmentName,SegmentSize,Mem,Start,Size):
    j=0
    token=0
    SegmentStart = []




    ################-------To Shamy Code----------------#####

    if Mem==[]:
        for i in range(len(HoleSize)):
            Mem.append("hole")
            Start.append(HoleStarting[i])
            Size.append(HoleSize[i])
        if Start[0]>0:
            Mem.insert(0,"PreAllocated")
            Start.insert(0,0)
            Size.insert(0,Start[1])
        counter=0
        while counter <len(Mem)-1:
            if Mem[counter] == "hole"  and Start[counter+1] > (Start[counter]+Size[counter]):
                Mem.insert(counter+1,"PreAllocated")
                Start.insert(counter+1,(Start[counter]+Size[counter]))
                Size.insert(counter+1,Start[counter+2]-Start[counter+1])
            counter += 1
        if Mem[len(Mem)-1]=="hole" and (Start[len(Mem)-1]+Size[len(Mem)-1])<TotalMemSize:
            Mem.append("PreAllocated")
            Start.append((Start[len(Mem)-2]+Size[len(Mem)-2]))
            Size.append((TotalMemSize-Start[len(Mem)-1]))


###########-------------------------------#####

    if Mem==[]:
        for i in range(len(HoleSize)):
            Mem.append("hole")
            Start.append(HoleStarting[i])
            Size.append(HoleSize[i])

    for i in range(len(SegmentName)):
        while j < (len(HoleStarting)):
            if SegmentSize[i] <= HoleSize[j]:
                for k in range(len(Size)):
                    if Mem[k]=="hole" and Size[k] >= SegmentSize[i]:
                        break
                Mem.insert(k,SegmentName[i])
                SegmentStart.append(HoleStarting[j])
                Start.insert(k,int(SegmentStart[i]))
                Size.insert(k,int(SegmentSize[i]))
                Size[k+1]=HoleSize[j]-SegmentSize[i]
                Start[k+1]= HoleStarting[j]+SegmentSize[i]
                HoleSize[j] = HoleSize[j]-SegmentSize[i]
                HoleStarting[j] = HoleStarting[j]+SegmentSize[i]
                if HoleSize[j] == 0:
                    del HoleSize[j]
                    del HoleStarting[j]
                    del Size[k+1]
                    del Start[k+1]
                    del Mem[k+1]
                   # NoOfDeletedHoles+=1
                j=0
                break                           # 3achan a5rog lw 7sl fit mydawwarch 3la holes tany

            elif j == len(HoleSize)-1:      #kda el segment not fit any hole
                 token= -1
            j += 1

    return Mem, Start, Size,token













##########################################################

'''
class Window(QWidget):
    def __init__(self, num_of_seg, process_number, seg_names, limit, base):
        super().__init__()
        self._num_of_seg = int(num_of_seg)
        self._process_number = process_number
        self._seg_names = seg_names
        self._limit = limit
        self._base = base
        self.title = self._process_number
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.creatingTables()

        self.show()

    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self._num_of_seg)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(('SegNumber', 'limit', 'Base'))
        seg_list = self._seg_names.split(',')
        limit_list = self._limit.split(',')
        base_list = self._base.split(',')
        for row in range(self._num_of_seg):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(seg_list[row]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(limit_list[row]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(base_list[row]))

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)
'''
class App(Frame):

    def __init__(self, parent, num_of_reg,  process_number, seg_names, limit, base):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.winfo_toplevel().title(process_number)
        self.LoadTable(num_of_reg, process_number, seg_names, limit, base)
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('limit', 'base', )
        tv.heading("#0", text='Seg_names', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('limit', text='limit')
        tv.column('limit', anchor='center', width=100)
        tv.heading('base', text='base')
        tv.column('base', anchor='center', width=100)

        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self, num_of_reg, process_number, seg_names, limit, base):
        for i in range(len(limit)):
            self.treeview.insert('', 'end', text=seg_names[i], values=(limit[i],
                                 base[i]))






















###  main  ###

Mem=[]
Start=[]
Size=[]
token=[]
v=-1
#total_size=0

#########











def open_window():
    top=Toplevel()






root=Tk()

################################matplotlib


#values=[30,60 ,20,30,20]
#y_names=["first" ,"second" ,"third"]
#sum_values =sum(values)


fig2, gnt = plt.subplots(figsize=(6,5))
canvas = FigureCanvasTkAgg(fig2, master=root )  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.Y, expand=1)



####################
    #pullData = open('sampleTextt.txt','r').read()
    #dataArray = pullData.split('\n')
    #val_str=dataArray[0].split(",")
    #values=[int(element) for element in val_str]
    #y_names=dataArray[1].split(",")
def drawing(Mem, Start, Size):
        values=Size
        sum_values =total_size
        y_names=Mem
        colors=["r","g","b"]
        out_edited=values  #[((total_size/sum_values)*x) for x in values]
        gnt.clear()
        print(out_edited)
        print (Mem)
        for i in range(0,len(values)):
            if Mem[i]=="hole":
                color="r"


            elif Mem[i]=="PreAllocated":
                color="m"
            else :
                color="g"
            gnt.bar([20],out_edited[i], bottom=np.sum(out_edited[:i], axis=0) ,color ='{}'.format(color),width=30)
            plt.text(y = ((np.sum(out_edited[:i+1])+np.sum(out_edited[:i]))/2) , x =18 , s=y_names[i], size =10)



        gnt.set_ylim(0, total_size)
        gnt.set_xlim(0, 40)

        gnt.set_xlabel('main memory')
        gnt.set_yticks(Start)
        gnt.set_yticklabels(Start)
        gnt.set_xticklabels([])



        gnt.grid(True)
#plt.show()





def animate(i):
    global v,Mem,Start,Size


    if v==-1:
        k=0
    elif v==0:
        #Mem, Start, Size, token = FirstFit(total_size, starting_hole_address, size_hole, name_process, name_segment, size_segment,Mem,Start,Size)
        drawing(Mem,Start,Size)

    elif v==1:
        k=0
        #best
    elif v==2:
        #Mem, Start, Size, token =AddAnotherProcess(total_size, starting_hole_address, size_hole, Mem, Start, Size)
        drawing(Mem,Start,Size)
        v=-1








##################################end of matplotlib

#total size


entry1=ttk.Entry(root,width=40)
entry1.pack()
u1=ttk.Button(root,text="enter total size")
u1.pack()
def buclik():
     a= entry1.get()
     global total_size
     total_size=int(a)

u1.config(command=buclik)


#### holes
#starting addrs
entry2=ttk.Entry(root,width=40)
entry2.pack()
u2=ttk.Button(root,text="enter holes starting")
u2.pack()
def buclikk():
    b = entry2.get()
    yy=[]
    yy=b.split(",")
    global HoleStarting
    HoleStarting=yy.copy()
    HoleStarting=[int(i) for i in HoleStarting]
u2.config(command=buclikk)

#size
entry3=ttk.Entry(root,width=40)
entry3.pack()
u3=ttk.Button(root,text="enter holes size")
u3.pack()
def buclikkk():
    c = entry3.get()
    y=[]
    y=c.split(",")
    global HoleSize
    HoleSize=y.copy()
    HoleSize=[int(i) for i in HoleSize]
u3.config(command=buclikkk)
#bu1=ttk.Button(root,text='show mem allocation with holes only')
#bu1.pack()
#bu6=ttk.Button(root,text='show table for holes')
#bu6.pack()

##name of procees
entry8=ttk.Entry(root,width=40)
entry8.pack()
u4=ttk.Button(root,text="enter name of process")
u4.pack()
def buclikkkk():
    d = entry8.get()
    global name_process
    name_process=d
u4.config(command=buclikkkk)
######

## enter num of segmants
entry5=ttk.Entry(root,width=40)
entry5.pack()
u6=ttk.Button(root,text="enter num of segmants")
u6.pack()
def buclikkkkkk():
    f = entry5.get()
    global num_of_segments
    num_of_segments=int(f)

u6.config(command=buclikkkkkk)


##########
### name of segement
entry4=ttk.Entry(root,width=40)
entry4.pack()
u5=ttk.Button(root,text="enter name of segement")
u5.pack()
def buclikkkkk():
    e = entry4.get()
    ee=[]
    ee=e.split(",")
    global name_segment
    global name_process
    name_segment=[]
    for i in range (len(ee)):
        name_segment.append(name_process +" "+ee[i])

    #name_segment=ee.copy()
u5.config(command=buclikkkkk)



###size of segemnts
entry6=ttk.Entry(root,width=40)
entry6.pack()
u7=ttk.Button(root,text="enter segemnts size")
u7.pack()
def bucliqq():
    h = entry6.get()
    hh=[]
    hh=h.split(",")
    global  size_segment
    size_segment=hh.copy()
    size_segment=[int(i) for i in size_segment]

u7.config(command=bucliqq)




'''
u9=ttk.Button(root,text="submit the new process ")
u9.pack()
def bucliqqqq():
    global v,Mem, Start, Size
    #v=2
    Mem, Start, Size, token =AddAnotherProcess(total_size, starting_hole_address, size_hole, Mem, Start, Size)

u9.config(command=bucliqqqq)

'''


'''
def table():
    c=0
    global Mem,Start,total_size, name_process, name_segment, size_segment, starting_address
    tablesss=[]
    starting_address=[]
    tablesss.clear()
    starting_address.clear()
    for i in range(len(Mem)-1):
        if((Mem[i]!='PreAllocated')&(Mem[i]!='hole')):
            tablesss.append(i)
    for j in range(len(Start)-1):
        if(c<len(tablesss)):
               if(j==tablesss[c]):
                  starting_address.append(Start[j])
                  c=c+1
    c=0
    rot = Tk()
    App(rot, total_size, name_process, name_segment, size_segment, starting_address)
    tablesss.clear()
    starting_address.clear()
    rot.mainloop()

bu2=ttk.Button(root,text='show table first fit')
bu2.pack()
bu2.config(command=table)
'''
bbb=0
def table():
    global bbb
    c=0
    global Mem,Start,total_size, name_process, name_segment, size_segment, starting_address,tablesss
    tablesss=[]
    starting_address=[]
    tablesss.clear()
    starting_address.clear()
    for i in range(len(Mem)-1):
        if((Mem[i]!='PreAllocated')&(Mem[i]!='hole')&(Mem[i][0:2]!='p'+str(bbb))):
            tablesss.append(i)
    bbb=bbb+1
    for j in range(len(Start)-1):
        if(c<len(tablesss)):
               if(j==tablesss[c]):
                  starting_address.append(Start[j])
                  c=c+1
    c=0
    rot = Tk()
    App(rot, total_size, name_process, name_segment, size_segment, starting_address)
    tablesss.clear()
    starting_address.clear()
    rot.mainloop()

bu2=ttk.Button(root,text='show table for this process')
bu2.pack()
bu2.config(command=table)






button4=ttk.Button(root,text='first fit')
button4.pack()
def first_fit_call():
    global v,Mem, Start, Size , token
    v=0


    Mem, Start, Size, token = FirstFit(total_size, HoleStarting, HoleSize, name_process, name_segment, size_segment,Mem,Start,Size)
    if (token == -1):
        messagebox.showinfo("error", "segment size is bigger than hole size ")
button4.config(command=first_fit_call)

button5=ttk.Button(root,text='best fit')
button5.pack()
def best_fit_call():
    global v,Mem, Start, Size
    v=0
    Mem, Start, Size, token = bestfit(total_size, HoleStarting, HoleSize, name_process, name_segment, size_segment,Mem,Start,Size)
    if (token == -1):
        messagebox.showinfo("error", "segment size is bigger than hole size ")
button5.config(command=best_fit_call)
###
entry44=ttk.Entry(root,width=40)
entry44.pack()
u55=ttk.Button(root,text="Deallocate")
u55.pack()
def bucli5():
    eei = entry44.get()
    global name,Mem, Start, Size
    name=eei
    Mem,Start,Size=DeAllocate(Mem, Start, Size,name)



    #name_segment=ee.copy()
u55.config(command=bucli5)
##########
'''
u556=ttk.Button(root,text="Check for error")
u556.pack()
def bucli556():
    global v,token
    if(token==1):
        messagebox.showinfo("error","don't do that")



    #name_segment=ee.copy()
u556.config(command=bucli556)
'''









#page1btn = ttk.Button(root, text="next", comman=open_window)
#page1btn.pack()

ani = animation.FuncAnimation(fig2,animate, interval=1000)
root.mainloop()


#####
#root.mainloop()











