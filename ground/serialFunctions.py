import serial
import struct
from dataclasses import dataclass

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

# very shitty (wrong) sample data package:
#b'\xff\xfff\x90\xe1AjJ\xc9B\x00@\x0e>\x00\x00\x06\xbd\x00\x80z?\x00\x80;\xbe\x00\xa0\x0c?\x00\x00z=\x00@N@\x00T\xd3A\x80\xd0\x06B\x00\x00\x00\x00\x00\x00\x00\x00\x87u\x14\x00\xa4U'

# "fake" and nice one:
raw =  b'\x31\x99\xc3\x41\xca\x15\xc8\x42\x00\x00\x03\x3d\x00\x00\x84\xbd\x00\x08\x7d\x3f\x00\x40\x9c\x3e\x00\xe8\x00\x40\x00\x00\x7a\x3e\x00\x86\x3a\x41\x80\x88\x12\x42\x00\x1f\x95\xc1\xd0\x46\x08\x42\x18\xe3\xec\xc2\x00\x00\x00\x00'


@dataclass
class RocketData:
    Hts_temperature : float = 0
    Lps_pressure : float = 0
    Imu_accelX : float = 0
    Imu_accelY : float = 0
    Imu_accelZ : float = 0
    Imu_gyroX : float = 0
    Imu_gyroY : float = 0
    Imu_gyroZ : float = 0
    Imu_magX : float = 0
    Imu_magY : float = 0
    Imu_magZ : float = 0
    Gps_lat : float = 0
    Gps_lng : float = 0
    timestamp : int = 0


def unpackData(package):
    # ========
    # takes in package (wihthout start and end bytes)
    # returns unpacked data
    # format <fffffffffffffI
    # ========

    unpacked = struct.unpack("<fffffffffffffI", package)

    return unpacked

def findPackage(serialPort):
    # =======
    # reads the serial port and picks out packages
    # feeds into unpackData
    # =======

    pass


'''

receive = serial.Serial()

receive.baudrate = 57600
receive.port = '/dev/tty.usbserial-AI02MK71'
receive.open()

package = receive.read(60)
print(package)



receive.close()

'''

data = RocketData()
unpacked = unpackData(raw)

# https://stackoverflow.com/questions/1993727/expanding-tuples-into-arguments
# this is so epic holy shit python

# how to update the class?
_data = RocketData(*unpacked)
data = _data

print(data)
