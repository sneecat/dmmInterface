from tkinter import *
from tkinter import ttk
def update():
   fart.set(fart + 'fart')


root = Tk()
root.title('Siglent 3045x')

mainframe = ttk.Frame(root, padding='2 2 12 12')
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fart = StringVar()
ttk.Label(mainframe, textvariable=fart).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Update", command=update).grid(column=1, row=1, sticky=W)



root.mainloop

