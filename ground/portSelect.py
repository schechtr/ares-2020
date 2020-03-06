import serial.tools.list_ports
import sys
import glob
import serial

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.usb*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port, timeout=.000001)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


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
        
    