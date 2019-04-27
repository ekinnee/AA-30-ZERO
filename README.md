# AA-30-ZERO
Control a RigExpert AA-30 ZERO from a Nextion 2.8" HMI LCD using an Arduino


# CopySerial
Upload this to your Arduino Uno. All it does it move data from the AA-30 to serial and back.
Same thing as shown in the "Getting Started" on RigExert's site.

# aa30.py
A Python script that listens for input from the Nextion on the serial port and causes the AA-30 ZERO
to analyze the specified Amateur Radio band frequency's SWR rating given the connected antenna and measure its reactance.

# TODO
Make the LCD work

Output commands from the LCD over serial

Interpret those commands in the Python scipt, send the coresponding command to the AA-30

Inpterpret and plot the return data from the AA-30 on a Waveform on the LCD

Possibly integrate https://github.com/vsergeev/rigexpert-tool rather than "re-invent the wheel"