import os
import pandas as pd

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def deleteAll():
    tree.delete(*tree.get_children())

def openData():
    file = filedialog.askopenfilename()
    if file == '':
        return
    
    deleteAll()

    data = pd.read_csv(file)
    cols = data.columns.tolist()

    tree.configure(columns=cols)

    for col in cols:
        tree.heading(col, text=col)

    for i in range(0, data.count(axis=0, numeric_only=True).iloc[0]):
        row = []

        for col in cols:
            row.append(data.at[i, col])

        tree.insert('', 'end', values=row)

screen_size = (800, 600)

root = Tk()
root.title("TableLooker")
root.geometry(f'{screen_size[0]}x{screen_size[1]}')
root.option_add("*tearOff", FALSE)

menubar = Menu(root)
menu_file = Menu(menubar)
menu_edit = Menu(menubar)

menubar.add_cascade(menu=menu_file, label="File")
menubar.add_cascade(menu=menu_edit, label="Edit")

menu_file.add_command(label="Open...", command=openData)

menu_edit.add_command(label="Delete All", command=deleteAll)

root["menu"] = menubar

frame = ttk.Frame(root, padding="4 4 4 4", width=screen_size[0], height=screen_size[1])
frame.grid(column=0, row=0, sticky="nwes")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

columns = [chr(abc) for abc in range(65, 91)]

tree = ttk.Treeview(frame, columns=columns, show='headings')
tree.grid(row=0, column=0, sticky="news")

for h in columns:
    tree.heading(h, text=h)

scrollbar_x = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
scrollbar_y = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)

scrollbar_x.grid(row=1, column=0, sticky="we")
scrollbar_y.grid(row=0, column=1, sticky='ns')

tree.configure(xscrollcommand=scrollbar_x.set)
tree.configure(yscrollcommand=scrollbar_y.set)

root.mainloop()
