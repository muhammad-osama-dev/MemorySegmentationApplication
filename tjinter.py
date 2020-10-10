from tkinter import *
from tkinter import ttk

root = Tk()

tree = ttk.Treeview(root)

tree["columns"] = ("one", "two")
tree.column("one", width=150)
tree.column("two", width=100)
tree.heading("one", text="Limit")
tree.heading("two", text="Base")
### insert format -> insert(parent, index, iid=None, **kw)
### reference: https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview
tree.insert("", 0, text="Seg1", values=("55", "6"))
tree.insert("", "end", text="Seg2", values=("3", "2"))



tree.pack()
root.mainloop()


mainloop()