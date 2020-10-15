import tkinter as tk
from tkinter import ttk
import re
import pyvisa
import threading
from time import sleep
rm = pyvisa.ResourceManager()
scpiUSBport = 'USB0::0xF4EC::0xEE38::SDM34FBX4R0437::INSTR'
scpi_TCP_IP = 'TCPIP::192.168.1.120::INSTR'


class scpiThread():
    ''' wrapper for managing SCPI connection
        '''
    def __init__(self, port, interval=None):
        self.port = port
        self.interval = interval
        self.instrument_mode = 'VOLT'
        
        self.range = 'DC? 60'
        try:
            self.instrument = rm.open_resource(scpiUSBport)
        except pyvisa.errors.VisaIOError:
            self.reconnect_loop(3)
            self.mode_get()
        else:
            self.mode_get()
        
        
    def reconnect_loop(self, interval=2, timeout=None):
        ''' reconnect_loop will try to reconnect to the instrument if
        connection is lost, raise the "disconnected" flag,
        and eventually timeout if a value is given
        '''            
        disconnected = True
        while disconnected is True:
            try:
                rm.open_resource(self.port).query('*IDN?')
            except pyvisa.errors.VisaIOError:
                
                'Cannot connect to instrument. Trying again in %s seconds' % (interval)
                sleep(interval)
            else:
                self.instrument = rm.open_resource(scpiUSBport)
                disconnected = False
                return
    def mode_get(self):
        # this ugly POS is how python strips numbers & symbols using regex

         try:
            #query instrument for its current mode
            self.instrument_mode = self.instrument.query('MEAS?')
            #get rid of unneeded char and whitespace
            self.instrument_mode = self.instrument_mode[1:5].strip()

            
            return self.instrument_mode
           
         except pyvisa.errors.VisaIOError:
            self.reconnect_loop(3)
            
   
    def mode_set(self, mode):
        self.instrument.write(mode)
    
    def reading(self):
        
        try:
            query = 'MEAS:' + self.instrument_mode + ':' + self.range
            reading = round(float(self.instrument.query(query)), 2)
            print(str(reading) + ' ' +self.instrument_mode)

        except pyvisa.errors.VisaIOError:
            self.reconnect_loop()
    
    

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
siglent = scpiThread(scpiUSBport, 100)
def main():
    while 1:
        
        siglent.reading()
if __name__ == '__main__':
    main()