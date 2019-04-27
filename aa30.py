#!/usr/bin/env python

import atexit
import os
import re
import time
import serial

#Define the ham bands
Band = { 'OneSixty' : ['fq1900000', 'sw200000' , 'frx20'],\
          'Eighty' : ['fq3750000', 'sw500000', 'frx50'],\
          'Sixty' : [['fq5331900', 'sw2800', 'frx3'],\
                    ['fq5347900', 'sw2800', 'frx3'],\
                    ['fq5358900', 'sw2800', 'frx3'],\
                    ['fq5404900', 'sw2800', 'frx3']],\
          'Forty' : ['fq7150000', 'sw3000000', 'frx35'],\
          'Thirty' : ['fq10125000', 'sw50000', 'frx10'],\
          'Twenty' : ['fq14150000', 'sw300000', 'frx30'],\
          'Seventeen' : ['fq18118000', 'sw100000', 'frx10'],\
          'Fifteen' : ['fq21225000', 'sw450000', 'frx45'],\
          'Twelve' : ['fq24940000', 'sw100000', 'frx10'],\
          'Ten' : ['fq28985000', 'sw1970000', 'frx50'] 
}

#Serial port
ser = serial

#Register atexit to close the serial port nicely
atexit.register(exit_handler)

def exit_handler():
    ser.close()

#Handle the command to get the SWR readings for the given band
def GetSWR(band):
     if band == 'Sixty':
          for channel in Band[band] :
               for swrreq in channel :
                    SendCmd(swrreq)
     else:
          for swrreq in Band[band]:
               SendCmd(swrreq)

#Write the commands to the AA-30 one at a time pausing after each
def SendCmd(cmd):
     ser.write(bytes((cmd + '\r\n'), "ascii"))
     time.sleep(.3)

#Currently only print out the return from the SWR readings and ERROR conditions
def FromAA(data):
     if re.match('(.+?),(.+?),(.+)', data) is not None or re.match('ERROR', data) is not None:
          # For now just printing data
          print(data)

#Init stuff
if __name__== '__main__':
     ser = serial.Serial('COM15', baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=20, xonxoff=0, rtscts=0)

     #Testing
     GetSWR('Sixty')

#Main loop that handles return data from the serial port
while ser.is_open:
     FromAA(ser.readline().decode("ascii", "ignore").strip())
