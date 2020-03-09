
import serial
import serialParser
from portSelect import serial_ports


def main():
    
    print('Scanning ports...')    
    # select the port
    ports = serial_ports()
    print(ports)

    indexNum = int(input("Select index: "))
    port = ports[indexNum]
    
    receive = serial.Serial(port, baudrate=57600, timeout=5)
    print("Connection successful, listening on", port)
    
    # class instances
    data = serialParser.RocketData()
    parser = serialParser.SerialParser(data)

    while True:
        stream = receive.read(2400)
        
        parser.findPackage(stream)

        if len(parser.data_queue) > 25:
            break

        
    print("report:")
    print(parser.data_queue)
    print("total packages received: {}".format(parser.numpackages))
    print("total packages lost: {}".format(parser.loss))
    print("percent lost: {}".format(100.0 * parser.loss / parser.numpackages))

    
    receive.close()

    

if __name__ == "__main__":
    main()

