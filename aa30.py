#!/usr/bin/env python
import time
import os
from time import sleep
import serial
import re

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

swr = 0
swr_data = ()
ser = serial

def GetSWR(band):
     if band == 'Sixty':
          for channel in Band[band] :
               for swrreq in channel :
                    SendCmd(swrreq)
     else:
          for swrreq in Band[band]:
               SendCmd(swrreq)

def SendCmd(cmd):
     ser.write(bytes((cmd + '\r\n'), "ascii"))
     time.sleep(.3)

def FromAA(data):
     print(data)

if __name__== '__main__':
     ser = serial.Serial('COM15', baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=20, xonxoff=0, rtscts=0)

     GetSWR('Sixty')

while ser.is_open:
     line = ser.readline().decode("ascii", "ignore").strip()

     if re.match('(.+?),(.+?),(.+)', line) is not None or re.match('ERROR', line) is not None:
          FromAA(line)

ser.close()
