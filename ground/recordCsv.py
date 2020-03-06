import csv
from serialFunctions import RocketData
import datetime


def press2Alt(pressure, temp):
    '''
    temperature: Celsius
    pressure: hPa
    returns height in meters
    '''
    seaLevel = 1013.25
    pressure *= 10 #convert kpa to hpa
    return (pow(seaLevel/pressure, 1/5.257) - 1) * (temp + 273.15) * 1/(0.0065)

def convertPackage(packet : RocketData):
    '''
    takes in the Rocket dataclass
    returns a list in the order of the class 
    [
        Hts_temperature : float = 0 #celsius
        Lps_pressure : float = 0 # kiloPascals
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
        UNIX time : string %H:%M:%S
        altitude: float in meters
        Unix 
    ]
    '''
    results = list()
    for i in packet.__dict__.items():
        if i[0] == 'start' or i[0] == 'end':
            continue
        results.append(i[1])
    
    alt = press2Alt(results[1], results[0])
    alt = float("{0:.2f}".format(alt))
    results.append(alt)

    localtime = 
    return results

    

