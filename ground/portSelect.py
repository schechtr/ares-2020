import serial.tools.list_ports

def port_select():
    '''
    finds viable Serial ports for you
    returns the good port
    '''
    ports = serial.tools.list_ports.comports()
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
        
    