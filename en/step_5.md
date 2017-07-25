## Finding the USB port

For the micro:bit to be able to communicate with Scratch, you need to know how the micro:bit is connected to the Raspberry Pi.

- With the micro:bit **disconnected** from the Raspberry Pi, open up LXTerminal and type the following:

    ```bash
	ls /dev/ttyA*
    ```

- Plug your micro:bit in via the USB cable and type the command again:

    ```bash
	ls /dev/ttyA*
    ```

- There should be a new entry in the output, probably something like `dev/ttyACM1`. You need to note this down.

