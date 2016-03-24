# BBC micro:bit game controller

In this resource, you'll use a micro:bit as a game controller in Scratch, and help take back control of the Galaxy

## Setting up the micro:bit

If you are unfamiliar with using the micro:bit, MicroPython and the Raspberry Pi, you might want to take a look at the [Getting Started with the micro:bit](https://www.raspberrypi.org/learning/getting-started-with-microbits) resource.

Also make sure you have the python3 scratch library and mu installed, as detailed in the [software setup guide](software.md)

## Finding the USB port

For the micro:bit to be able to communicate with Scratch, you need to know what how the micro:bit is connected to the Raspberry Pi.

1. With the micro:bit **disconnected from the Raspberry Pi, open up LXTerminal and type the following:

    ```bash
	ls /dev/ttyA*
    ```

1. Then plug in your micro:bit via the USB cable and type the command again.

    ```bash
	ls /dev/ttyA*
    ```

1. There should be a new entry in the output. Probably something like `dev/ttyACM1`
	
1. You need to note this down.

## Setting up the Python file

1. Open IDLE (`Menu`>`Programming`>`Python 3 (IDLE`), create a new file (`File`>`New File`), and copy and paste the code below into the file. Save it as `rpi.py`.

	```python
	import serial
	from time import sleep
	import scratch


	scr = scratch.Scratch()
	PORT = "/dev/ttyACM1"
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

1. This file (once running) will listen to any data being sent out from the micro:bit, and send it over to Scratch. You may have to change the line:

	```python
	PORT = "/dev/ttyACM1"
	```

    so it is the same as the port you noted down earlier.

## Coding the micro:bit

The microbit needs to be running some code that will constantly print out it's accelerometer readings and button pushes.

1. Open up **mu**, by opening LXTerminal and typing

	```bash
	./mu
	```

1. Now copy and paste the code below into the editor.

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

1. You can **Flash** this file into you microbit straight away.

## Setting up Scratch

1. Open up **Scratch** on the Raspberry Pi. (`Menu`>`Programming`>`Scratch`)

1. Go to `Sensing` and then near the bottom of the screen, right-click on `slider sensor value` and choose `enable remote sensor connections` from the context menu. Click on `OK` when the dialogue box opens.

![screen1](images/screen1.png)

1. No switch back over to IDLE and run (`F5`) your `rpi.py` script.

1. In Scratch you should now be able to view the values from the micro:bit's sensors. Simply click on the arrow on the `slider sensor value` block, choose `a` and then check the box.

![screen2](images/screen2.png)
![screen3](images/screen3.png)

1. If you repeat this for sensors `b`,`x`,`y` and `z`, then your Scratch stage should look something like this.

![screen4](images/screen4.png)

1. If you tilt the micro:bit you should see the `x`, `y` and `z` values changing. Pushing the buttons will switch `a` and `b` from `False` to `True`

1. If the readings aren't working, check the micro:bit port again, and make sure the code is running on both the micro:bit and the Raspberry Pi.

## Making the assets

You're going to need three new sprites for this game. Delete the *Cat* sprite and then use the web to find a *rocket* sprite, a *UFO* sprite and a *missile* sprite. You can use the ones below if you like, or even draw your own.

![rocket](images/rocket.png)
![ufo](images/ufo.png)
![missile](images/missile.png)

1. Import each of your sprites into Scratch.

![screen5](images/screen5.png)

1. Rename the sprites by changing the name in the *scripts pane*

![screen6](images/screen6.png)

1. The sprites will also need resizing. You can use the `shrink sprite` tool to do this

![screen7](images/screen7.png)

1. Lastly you should rotate the rocket and missile sprite, so they both point toward the right hand-side of the screen. Yo can do this by editing the sprite in the `costume` tab and choosing the `rotate` tool

![screen9](images/screen9.png)

![screen8](images/screen8.png)

## Coding the Rocket

1. To code your game, you can start by adding some scripts to the rocket. Because you want the game to be played over and over again, you can get the game to be started by a `broadcast` block. You'll also need to `make a variable` called `score` and set it to `0` at the start of the game.

![screen10](images/screen10.png)

1. To start the game the rocket need to be placed in the centre of the screen and pointing towards the right.

![screen11](images/screen11.png)

1. Next you need to control the rotation of the rocket. This is going to be decided by the accelerometer reading from the micro:bit. In particular the `x` sensor value. At the moment this is a value between about -1000 and 1000, so it needs to be reduced a little. Create a `new variable` called `turn` and set it as shown below.

![screen12](images/screen12.png)

1. Test out your game so far. When you tilt the micro:bit left and right, the rocket should spin around. If it is not working, try restarting the Python 3 program on your Raspberry Pi and re-flashing the micro:bit with it's program. You might also have to check that the microbit hasn't reconnected to a different port. `ls /dev/ttyA*`

1. Next you want the rocket to move. The speed can be determined by how far forwards or backwards the microbit has been tilted. You can use the `y` sensor value for this. But again, you need to reduce the value a little (an in this case reverse it.)

![screen13](images/screen13.png)

1. Test your flight controls now, by tilting the micro:bit left and right, forwards and backwards.

## Coding the UFO

1. The UFO needs to start in a random location and then chase after the Rocket. This is fairly easy to set up. The Scratch `Stage` stretches from about -250 to 250 horizontally (the x-axis) and -180 to 180 vertically (the y-axis). So picking two random numbers in these ranges, would position the rocket.

![screen14](images/screen14.png)

1. Next you can use a `forever` loop to get the UFO to chase the rocket.

![screen15](images/screen15.png)

1. In a minute you'll code the missile to launch at the UFO. If the missile hits the UFO, the game should restart and the player's score should go up by one. A new script is needed for this.

![screen16](images/screen16.png)

1. To finish off the UFO, the game needs to end if it catches the rocket.

![screen17](images/screen17.png)

## Coding the missile

1. To make the missile always point in the correct direction, you can make it turn exactly the same as the rocket.

![screen18](images/screen18.png)

1. Next, whenever the `A` button is pressed on the microbit, the missile needs to fire. To do this, you can move it to the location of the rocket, tell it to `show` and then move forwards until it hits either the UFO or the edge of the screen. It will need to carry on turning as if flies, otherwise the missile's rotation will become out of sync with the rocket.

![screen19](images/screen19.png)

1. Test out your rockets new ability to shoot missiles.

## What Next?

The game has plenty of potential to be improved.
- Can you add in some obstacles for the rocket and UFO to avoid?
- You still have the `B` button to be used. Maybe this could start a **Turbo** mode where the rocket flies even faster.
- Could the UFO have a laser beam that it shoots at the rocket every now and then.

