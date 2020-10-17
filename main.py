import tkinter as tk
from tkinter import ttk
import re
import pyvisa
# TODO: Make scpithread work with threading lol
import threading
from time import sleep
rm = pyvisa.ResourceManager()

scpiUSBport = 'USB0::0xF4EC::0xEE38::SDM34FBX4R0437::INSTR'
scpi_TCP_IP = 'TCPIP::192.168.1.120::INSTR'

valid_mode_dict = {
    'VOLT': ':DC? 60',
    'CURR': ':DC? 6',
    'RES': '? AUTO',
    'DIOD': '?',
    'CONT': '?',
    'CAP': '? AUTO'
}

class scpiThread():
    ''' wrapper for managing SCPI connection
        '''
    def connect(self, interval = 3):
        
        try:

            self.instrument = rm.open_resource(scpiUSBport)
            self.instrument.write_termination = '\r'
            self.instrument.read_termination = '\n'
            self.instrument.query_delay = .1
        
        except pyvisa.errors.VisaIOError:
            disconnected = True
            
            while disconnected is True:
                try:
                    rm.open_resource(self.port).query('*IDN?')

                except pyvisa.errors.VisaIOError:
                    'Cannot connect to instrument. Trying again in %s seconds' % (interval)
                    sleep(interval)

                else:
                    disconnected = False
                    self.connect()
                    
    def __init__(self, port, interval=None):
        self.port = port
        self.interval = interval
        self.instrument_mode = 'VOLT'
        self.instrument_range = 'DC? 60'
        self.connect()
        self.mode_get()
    
    def mode_get(self):

         try:
            #query instrument for its current mode
            self.instrument_mode = self.instrument.query('CONF?')
            #get rid of unneeded char and whitespace
            self.instrument_mode = self.instrument_mode[1:5].strip()

            
            return self.instrument_mode
           
         except pyvisa.errors.VisaIOError:
            self.connect()
            
   
    def mode_set(self, mode):
        if mode in valid_mode_dict and valid_mode_dict[mode]:
            self.instrument_mode = mode
            self.instrument_range = valid_mode_dict.get(mode)
            self.instrument.write('CONF:' + mode)
        else:
            print('Not a valid mode. Please use VOLT, RES, CURR, DIOD, CAP, or CONT')

    def reading(self):
        
        try:
            query = 'MEAS:' + self.instrument_mode + self.instrument_range
            reading = round(float(self.instrument.query(query)), 2)
            if '9.9e+37' in reading:
                reading = 'O/L'
            else:
                print(str(reading) + ' ' + self.instrument_mode)

        except pyvisa.errors.VisaIOError:
            self.connect()
siglent = scpiThread(scpiUSBport, 100) 
    

# class gui():
#     '''
#         gui handler for updating display and sending commands from
#         buttons to scpi, starting and stopping the connection
#     '''
#     def __init___():
#         self.root = tk.Tk()
#         self.measurment = tk.StringVar()
#         self.wininit()

#     def wininit():
#         '''
#             initialize window
#         '''
#         self.root.title('Multimeter')
#         self.root.geometry('400x200-5+40')
#         self.root.resizable(FALSE,FALSE)
#         self.root.attributes("-topmost", 1)

siglent.mode_set('CONT')
def main():
    while 1:
        
        siglent.reading()
if __name__ == '__main__':
    main()