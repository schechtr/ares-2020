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

# real data package:
_real = '\xff\xfff\x90\xe1AjJ\xc9B\x00@\x0e>\x00\x00\x06\xbd\x00\x80z?\x00\x80;\xbe\x00\xa0\x0c?\x00\x00z=\x00@N@\x00T\xd3A\x80\xd0\x06B\x00\x00\x00\x00\x00\x00\x00\x00\x87u\x14\x00\xa4U'

# a fake but easy to test with one:
_package =  b'\x31\x99\xc3\x41\xca\x15\xc8\x42\x00\x00\x03\x3d\x00\x00\x84\xbd\x00\x08\x7d\x3f\x00\x40\x9c\x3e\x00\xe8\x00\x40\x00\x00\x7a\x3e\x00\x86\x3a\x41\x80\x88\x12\x42\x00\x1f\x95\xc1\xd0\x46\x08\x42\x18\xe3\xec\xc2\x00\x00\x00\x00'

_raw =  b'\xff\xff\x31\x99\xc3\x41\xca\x15\xc8\x42\x00\x00\x03\x3d\x00\x00\x84\xbd\x00\x08\x7d\x3f\x00\x40\x9c\x3e\x00\xe8\x00\x40\x00\x00\x7a\x3e\x00\x86\x3a\x41\x80\x88\x12\x42\x00\x1f\x95\xc1\xd0\x46\x08\x42\x18\xe3\xec\xc2\x00\x00\x00\x00\xa4\x55'\
        b'\xff\xff\x31\x98\xc2\x41\xca\x15\xc8\x42\x00\x00\x03\x3e\x00\x00\x84\xbd\x00\x08\x75\x3f\x00\x40\x9c\x3e\x00\xe8\x00\x40\x00\x00\x9a\x3e\x00\x86\x3a\x41\x80\x88\x12\x42\x00\x1f\x95\xc1\xd0\x46\x08\x42\x23\xe3\xec\xc2\x00\x00\x00\x00\xa4\x55'

@dataclass
class RocketData:
    start : bytes = ''
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
    end : bytes = ''


class SerialParser:

    def __init__(self, data):
        self.data = data
        self.data_queue = []
        
    
    def findPackage(self, stream):
        # =======
        # reads the serial data and picks out packages
        # feeds into unpackData
        # =======

        packages = stream.hex().split('ffff')
        
        for package in packages: 
            if package:
                package = 'ffff' + package
            
                unpacked = self.unpackData(bytes.fromhex(package))
                self.updateData(unpacked)


    def unpackData(self, package):
        # ========
        # takes in package (wihthout start and end bytes)
        # returns unpacked data as a tuple
        # format <fffffffffffffI
        # ========

        unpacked = struct.unpack("<2sfffffffffffffI2s", package)

        return unpacked


    def updateData(self, update):
        # =======
        # updates RocketData after newly unpacked data is available
        # =======

        data = RocketData(*update)
        self.data = data

        # thought a queue could be helpful maybe, at least for debugging it is
        self.data_queue.append(data)
        if len(self.data_queue) > 10:
            self.data_queue.pop(0)


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
parser = SerialParser(data)

'''
 if the serial stream was running here then data would come in and be parsed like this.
 idk if it will work exactly like this irl but we can see. definitely need some error checking
 with the start and end bytes and size of packages.
'''
parser.findPackage(_raw)

print(parser.data_queue)

