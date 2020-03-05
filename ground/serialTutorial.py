import serial
import struct


#=====================
# bytes 0, 1 are padding
# 2 temperature (4)
# 6 Lps_pressure
# IMU
# 10 X
# 14 Y
# 18 Z
# GYRO
# 22 X
# 26 Y
# 30 Z
# MAG
# 34 X 
# 38 Y 
# 42 Z
# GPS
# 46 lat
# 50 long
# Timestamp
# 58 time 
# 59 pad 
# 60  pad
#=========================

receive = serial.Serial()

receive.baudrate = 57600
receive.port = '/dev/tty.usbserial-AI02MK71'
receive.open()

package = receive.read(60)
print(package)




receive.close()