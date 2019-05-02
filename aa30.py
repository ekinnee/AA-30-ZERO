#!/usr/bin/env python3

#Copyright (C) 2019 Erick Kinnee erick@kinnee.net

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
#Tracker for serial port ready
ready = 0

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
    if re.match('Ready', data):
        ready = 1
    else:
        if re.match('(.+?),(.+?),(.+)', data) is not None:
            print(data)


#Basic handler for data from the LCD
def FromLcd(data):
    if ready == 0:
        pass
    else:
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
    #Open the serial port that the arduino is connected to.
    #The AA-30 ZERO only goes 38400 max
    ser = serial.Serial('/dev/ttyACM0', baudrate = 38400)
    ser.flushInput()
    ser.flushOutput()
    #8 seconds is just long enough for the Uno to reboot
    time.sleep(10)
    GetSWR('Twelve')

#Main loop that handles return data from the serial port
while True:
    if ser.inWaiting() > 0:
        FromSerial(ser.readline().decode("ascii", "ignore").strip())

def exit_handler():
    ser.close()

#Register atexit to close the serial port nicely
atexit.register(exit_handler)
