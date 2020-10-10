import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import tkinter
from tkinter import *
from tkinter import ttk



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
        for i in range(num_of_reg):
            self.treeview.insert('', 'end', text=seg_names[i], values=(limit[i],
                                 base[i]))

root = Tk()
App(root, 3, 'p2', ['seg1', 'seg2', 'seg3'], [5, 6, 7] ,[7 , 6 , 8])
root.mainloop()
