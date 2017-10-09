## Setting up the micro:bit

If you are unfamiliar with using the micro:bit, MicroPython, and the Raspberry Pi, you might want to take a look at the [Getting Started with the micro:bit](https://projects.raspberrypi.org/en/projects/getting-started-with-microbit) resource first.

For the micro:bit to be able to communicate with Scratch, you need to know how the micro:bit is connected to the Raspberry Pi.

+ Make sure the micro:bit is **disconnected** from the Raspberry Pi

+ Open a terminal and type the following:

```bash
ls /dev/ttyA*
```

+ Connect one end of the USB cable to your micro:bit and the other to the Raspberry Pi, then type the same command again:

```bash
ls /dev/ttyA*
```

+ Look at the output from both times you ran the command. Note down the new entry that appears the second time (it is probably something like `/dev/ttyACM0`).
