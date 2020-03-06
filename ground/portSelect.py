import serialFunctions
import glob

# def portSelect():
#     '''
#     finds viable Serial ports for you
#     returns some
#     '''

import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

USB_DIRECTORY = '/dev/cu.usb*'

# try:
#     ports = glob.glob(USB_DIRECTORY)
#     if len(ports) > 1:
#         print('More than one USB device detected. Please disconnect all other USB devices')

#     serial_ports = ports[0]

#     print(ports)
# except:
#     print('Could not find a usb device')


# print("Found the following ports:")

# for port, desc, hwid in sorted(ports):
#     print("{}: {} [{}]".format(port, desc, hwid))

def port_select():

    print("hamlin has a small pp")

    serial_ports = list()
    for port in sorted(ports):
        if port.description != 'n/a':
            serial_ports.append(port)

    if not serial_ports:
        raise Exception("Could not find a USB serial device")
    elif len(serial_ports) > 1:
        raise Exception("Error: found more than one USB serial device")

    else:
        print("Found a USB serial port:")
        good_port = serial_ports[0]
        print("{}: {} [{}]".format(good_port.device, good_port.description, good_port.hwid))

        del serial_ports

        return good_port
        
    