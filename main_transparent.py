import tkinter as tk
from tkinter import *
from tkinter import ttk

import pyvisa

import easy_scpi as scpi




def update():
    
    reading.set(round(float(sig.query('read?')), 4))
    label_reading.after(200, update)
    



root = tk.Tk()
root.title('DMM')
root.geometry('475x200-5+40')
reading = tk.StringVar()
root.resizable(FALSE,FALSE)
root.attributes("-alpha", 1)
root.attributes("-topmost", 1)
frame = tk.Frame(root)
frame.grid(column=2, row=2, sticky=(N,W,E,S))

label_reading = ttk.Label(frame, text='volts', textvariable=reading, width=300)
label_reading.grid(row=2, column=0, padx=5, pady=5)
label_reading.config(font=("Courier", 70))
label_volts = ttk.Label(frame, text='volts')
label_volts.grid(row=1, column=0, padx=5, pady=5)
voltB = ttk.Button(





#create resource manager for pyvisa
rm = pyvisa.ResourceManager()
# try to talk to the siglent, throw an exception if u cant
try:
    sig = rm.open_resource('USB0::0xF4EC::0xEE38::SDM34FBX4R0437::INSTR')
except:
    print('Siglent DMM was not found. Check USB connection')
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

