## Setting up the Python file

- Open IDLE (**Menu** > **Programming** > **Python 3**), create a new file (**File** > **New File**), and copy and paste the code below into the file. Save it as `rpi.py`.

	```python
	import serial
	from time import sleep
	import scratch


    scr = scratch.Scratch()
    ## THE NEXT LINE MIGHT NEED TO BE CHANGED - TYPE ls /dev/ttyA* into the terminal to see which port is needed.
	PORT = "/dev/ttyACM1"
	## 
	BAUD = 115200

	s = serial.Serial(PORT)
	s.baudrate = BAUD
	s.parity   = serial.PARITY_NONE
	s.databits = serial.EIGHTBITS
	s.stopbits = serial.STOPBITS_ONE

	while True:
		data = s.readline().decode('UTF-8')
		data_list = data.rstrip().split(' ')
		try:
		    x, y, z, a, b = data_list
			scr.sensorupdate({'x' : x})
			scr.sensorupdate({'y' : y})
			scr.sensorupdate({'z' : z})
			scr.sensorupdate({'a' : a})
			scr.sensorupdate({'b' : b})

		except:
			pass

	s.close()
	```

- This file, once running, will listen to any data being sent out from the micro:bit, and send it over to Scratch. You may have to change this line:

	```python
	PORT = "/dev/ttyACM1"
	```
	
It needs to be the same as the port you noted down earlier.

