#!/usr/bin/python2
# Simple user input for interacting with the Arduino.

import time
import serial

# Configure the serial
ser = serial.Serial(
        port='/dev/tty.usbmodem1421',
        baudrate=115200
)

print 'Enter your commands below.'
print 'Insert "exit" to leave the application or "help" for a list of commands.'

input=1
while ser.isOpen():
    # Get keyboard input
    input = raw_input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    elif input == 'help':
        print 'Possible commands:'
        print '\tread light'
        print '\tread moisture'
        print '\tread status'
        print '\twrite on'
        print '\twrite off'
    else:
        # send to the Arduino
        ser.write(input + '\r\n')
        out = ''
        # give device time to answer
        time.sleep(0.2)
        while ser.inWaiting() > 0:
            out += ser.read(1)
        # output response
        if out != '':
            print out
