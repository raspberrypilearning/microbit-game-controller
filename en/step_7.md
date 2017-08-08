## Coding the micro:bit

The micro:bit needs to run some code that will constantly print out its accelerometer readings and button pushes.

- Open mu by opening LXTerminal and typing the following command:

	```bash
	./mu
	```

- Now copy and paste the code below into the editor:

	```python
	from microbit import *

	def get_sensor_data():
		x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
		a, b = button_a.was_pressed(), button_b.was_pressed()
		print(x, y, z, a, b)


	while True:
		sleep(100)
		get_sensor_data()

	```

- You can flash this file into your micro:bit straight away.

