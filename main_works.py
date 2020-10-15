import tkinter as tk
from tkinter import *
from tkinter import ttk

import pyvisa






def update():
    print('update begin')
    reading.set(round(float(sig.query('read?')), 2))
    label_reading.after(100, update)
    
    print('update')



root = tk.Tk()
root.title('fartbox')
root.overrideredirect(True)
root.geometry('400x120-15+20')
root.lift()
reading = tk.StringVar()
root.resizable(FALSE,FALSE)
root.attributes("-topmost", 1)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")
label_volts = ttk.Label(root, foreground = 'grey', background='white', text='VOLTS', width=400)
label_reading = ttk.Label(root, foreground='grey', background='white', text='VOLTS', textvariable=reading, width=300)
label_volts.config(font=("Courier", 30))
label_volts.pack()
label_reading.config(font=("Courier", 60))
label_reading.pack()





#create resource manager for pyvisa
rm = pyvisa.ResourceManager()
# try to talk to the siglent, throw an exception if u cant
try:
    sig = rm.open_resource('USB0::0xF4EC::0xEE38::SDM34FBX4R0437::INSTR')
except:
    print('dmm not found, check port')
    raise
#set command delimters
sig.write_termination = '\n'
sig.read_termination = '\n'
#ask for ID to confirm connection
sig.query('*IDN?')
# starting out with just voltage settings for now
sig.write('conf:volt:DC 60')
sig.write('samp:coun 1')


    

update()
root.mainloop()

