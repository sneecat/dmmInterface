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


