import serial
from time import sleep
import scratch


scr = scratch.Scratch()
PORT = "/dev/ttyACM3"
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE
s.readline()

while True:
    data = s.readline().decode('UTF-8')
    data_list = data.rstrip().split(' ')
    try:
        x, y, z, a, b = data_list
    except:
        pass

    scr.sensorupdate({'x' : x})
    scr.sensorupdate({'y' : y})
    scr.sensorupdate({'z' : z})
    scr.sensorupdate({'a' : a})
    scr.sensorupdate({'b' : b})    
    
s.close()
