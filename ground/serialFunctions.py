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