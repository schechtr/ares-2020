
import serial
import queue
import threading
import serialParser
from portSelect import serial_ports

q = queue.Queue()
# class instances
data = serialParser.RocketData()
parser = serialParser.SerialParser(data)

def worker():
    buf = b''
    while True:

        if q.empty():
            continue
        
        item = q.get()
        buf += item

        # call parser here but better
        if len(buf) > 1024:
            parser.findPackage(buf)
            buf = b''


def main():
    
    # select the port to read from
    print('Scanning ports...')    
    ports = serial_ports()
    print(ports)

    indexNum = int(input("Select index: "))
    port = ports[indexNum]
    
    ser = serial.Serial(port, baudrate=57600, timeout=5)
    print("Connection successful, listening on", port)

    
    # start parser thread
    parserThread = threading.Thread(target=worker)
    parserThread.start()


    while True:
        if ser.in_waiting > 0:
            read = ser.read(ser.in_waiting)
            q.put(read)

    

    # generate reports 
    print("report:")
    print(parser.data_queue)
    print("total packages received: {}".format(parser.numpackages))
    print("total packages lost: {}".format(parser.loss))
    print("percent lost: {}".format(100.0 * parser.loss / parser.numpackages))


    ser.close()

    

if __name__ == "__main__":
    main()

