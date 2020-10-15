import tkinter as tk
from tkinter import *
from tkinter import ttk
from threading import Timer
from threading import Thread
import time
from time import sleep

import pyvisa
import time

starttime = time.time()


        
        
def updateReading():
    reading.set(sig.query_ascii_values('read?'))

    
#PYVISA SETUP
# create resource manager
rm = pyvisa.ResourceManager()

# try to talk to the siglent, throw an exception if u cant
try:
    sig = rm.open_resource('USB0::0xF4EC::0xEE38::SDM34FBX4R0437::INSTR')

except:
    print('Siglent DMM was not found. Check USB connection')


sig.write_termination = '\n'
sig.read_termination = '\n'
sig.query('*IDN?')
sig.write('conf:volt:DC 60')
sig.write('samp:coun 1')
#TK SETUP


root = Tk()
root.title('Siglent 3045x')

mainframe = ttk.Frame(root, padding='2 2 12 12')

mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

reading = StringVar()
ttk.Label(mainframe, textvariable=reading).grid(column=2, row=2, sticky=(W, E))

mainframe.update()

root.mainloop
