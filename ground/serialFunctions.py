import serial
import struct

'''
=====================
bytes 
0 pad
1 pad
2 temperature (4)
6 Lps_pressure
IMU
10 X
14 Y
18 Z
GYRO
22 X
26 Y
30 Z
MAG
34 X 
38 Y 
42 Z
GPS
46 lat
50 long
Timestamp
54 time 
59 pad 
60  pad
=========================

sample data package:
b'\xff\xfff\x90\xe1AjJ\xc9B\x00@\x0e>\x00\x00\x06\xbd\x00\x80z?\x00\x80;\xbe\x00\xa0\x0c?\x00\x00z=\x00@N@\x00T\xd3A\x80\xd0\x06B\x00\x00\x00\x00\x00\x00\x00\x00\x87u\x14\x00\xa4U'
'''

def parser(package):
    # ========
    # takes in package
    # returns list of all data values
    # ========
    bytesSeparated = []
    for i in range(2, 59, 4):
        bytesSeparated.append(package[i:i + 4])
    
    returnedList = [];
    for i in bytesSeparated:
        if(i == bytesSeparated[-1]):
            returnedList.append(struct.unpack('<I', i)[0])
        else:
            returnedList.append(struct.unpack('<f', i)[0])
    return returnedList


def findPackage(serialPort):
    


receive = serial.Serial()

receive.baudrate = 57600
receive.port = '/dev/tty.usbserial-AI02MK71'
receive.open()

package = receive.read(60)
print(package)




receive.close()