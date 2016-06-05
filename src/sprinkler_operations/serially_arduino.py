import time
import serial


# ser = serial.Serial(
#         port='/dev/tty.usbmodem1421',
#         baudrate=115200
# )

#print 'Enter your commands below.'
#print 'Insert "exit" to leave the application or "help" for a list of commands.'

#
# 'Possible commands:'
#      'read light'
#      'read moisture'
#      'read status'
#      'write on'
#      'write off'

class ArduinoValues():
    def __init__(self, port='/dev/tty.usbmodem1421', baudrate=115200):
        self.laptop_serial = serial.Serial(port=port, baudrate=baudrate)

    def get_arduino_attr(self):
        # if self.laptop_serial.is_open:
        #     data = ("read {0}\r\n".format(data))
        #     temp = "read light\r\n"
        #     self.laptop_serial.write(temp)
        #     time.sleep(0.3)
        #     out = ''
        #     while self.laptop_serial.inWaiting() > 0:
        #         out += self.laptop_serial.read(1)
        #         hello = 'debug'
        #     return out
        # else:
        #     return "Error I can't connect Arduino :("

        ser = self.laptop_serial
        input=1
        for i in range(0,2):
            ser.write('read moisture' + '\r\n')
            out = ''
            # give device time to answer
            time.sleep(0.2)
            while ser.inWaiting() > 0:
                out += ser.read(1)
            # output response
            if out != '':
                print out

# a = ArduinoValues()
# a.get_arduino_attr()


# input=1
# while ser.isOpen():
#     # Get keyboard input
#     input = raw_input(">> ")
#     if input == 'exit':
#         ser.close()
#         exit()
#     elif input == 'help':
#         print 'Possible commands:'
#         print '\tread light'
#         print '\tread moisture'
#         print '\tread status'
#         print '\twrite on'
#         print '\twrite off'
#     else:
#         # send to the Arduino
#         ser.write(input + '\r\n')
#         out = ''
#         # give device time to answer
#         time.sleep(0.2)
#         while ser.inWaiting() > 0:
#             out += ser.read(1)
#         # output response
#         if out != '':
#             print out
