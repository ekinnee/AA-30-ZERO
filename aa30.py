#!/usr/bin/env python3

import atexit
import os
import re
import time
import serial

#Define the ham bands
Band = { 'OneSixty' : ['fq1900000', 'sw200000' , 'frx20'], \
          'Eighty' : ['fq3750000', 'sw500000', 'frx50'], \
          'Sixty' : [['fq5331900', 'sw2800', 'frx3'], \
                    ['fq5347900', 'sw2800', 'frx3'], \
                    ['fq5358900', 'sw2800', 'frx3'], \
                    ['fq5404900', 'sw2800', 'frx3']], \
          'Forty' : ['fq7150000', 'sw3000000', 'frx35'], \
          'Thirty' : ['fq10125000', 'sw50000', 'frx10'], \
          'Twenty' : ['fq14150000', 'sw300000', 'frx30'], \
          'Seventeen' : ['fq18118000', 'sw100000', 'frx10'], \
          'Fifteen' : ['fq21225000', 'sw450000', 'frx45'], \
          'Twelve' : ['fq24940000', 'sw100000', 'frx10'], \
          'Ten' : ['fq28985000', 'sw1970000', 'frx50']
}

#Serial port
ser = serial
ama = serial

def Error():
     pass

def RebootPi():
     os.system('sudo shutdown -r now')

def ShutdownPi():
     os.system('sudo shutdown -P now')

def ResetLcd():
     pass

def GotoLcdPage():
     pass

#Write the commands to the AA-30 one at a time pausing after each
def SendCmd(cmd):
     ser.write(bytes((cmd + '\r\n'), "ascii"))
     time.sleep(.3)

#Handle the command to get the SWR readings for the given band
def GetSWR(band):
     #60m in the US is weird
     if re.match('Sixty', band):
          for channel in Band[band] :
               for swrcmd in channel :
                    SendCmd(swrcmd)
     else:
          for swrcmd in Band[band]:
               SendCmd(swrcmd)

#Basic handler for data from the AA-30.
def FromSerial(data):
     if re.match('ERROR', data):
          Error()
     #Not a command, must be return data.
     else:
          if re.match('(.+?),(.+?),(.+)', data) is not None:
               # For now just printing data
               print(data)


#Basic handler for data from the LCD
def FromLcd(data):
     #Command data is formatted <command>:<param>
     if re.match('reboot', data):
          RebootPi()
     if re.match('power', data):
          ShutdownPi()
     if re.match('swr', data):
          data = data.replace('swr', '')
          for b in Band:
               if Band[b] == data:
                    GetSWR(data)

#Init stuff
if __name__== '__main__':
     #Open the serial port that the arduino is connected to. The AA-30 ZERO only goes 38400 max
     ser = serial.Serial()
     ser.port = 'COM8'
     ser.baudrate = 38400
     ser.open()
     
     #Testes Testes 1. 2. 4.
     ser.write(b'VER\r\n')

#Main loop that handles return data from the serial port
while True:
     #FromSerial(ser.readline().decode("ascii", "ignore").strip())
     print(ser.readline())

def exit_handler():
    ser.close()

#Register atexit to close the serial port nicely
atexit.register(exit_handler)