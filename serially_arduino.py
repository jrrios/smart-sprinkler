#!/usr/bin/python2
import time
import serial

class ArduinoValues:
    def __init__(self, port='/dev/tty.usbmodem1421', baudrate=115200):
        self.ser = serial.Serial(port=port, baudrate=baudrate)

    def get_attr(self, input):
        for i in range(6):
             # Arduino expects ending '\r\n'
            input = 'read ' + input + '\r\n'
            # send to the Arduino
            self.ser.write(input)
            out = ''
            # give device time to answer
            time.sleep(0.1)
            while self.ser.inWaiting() > 0:
                out += self.ser.read(1)
            # output response
            if out != '':
                return out.strip()

    def set_sprinkler(self, val):
        out = 'write on' if val else 'write off'
        self.ser.write(out + '\r\n')

    def get_light(self):
        return self.get_attr('light')

    def get_moisture(self):
        return self.get_attr('moisture')

    def get_status(self):
        return self.get_attr('status')

    def get_all(self):

        return [self.get_attr(x) for x in ['moisture', 'status', 'moisture', 'light']]

a = ArduinoValues()
print(a.get_all())
