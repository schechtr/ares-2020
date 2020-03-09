import os
import csv
import serialParser
from datetime import datetime


def press2Alt(pressure, temp):
    '''
    temperature: Celsius
    pressure: hPa
    returns height in meters
    '''
    seaLevel = 1013.25
    pressure *= 10 #convert kpa to hpa
    return (pow(seaLevel/pressure, 1/5.257) - 1) * (temp + 273.15) * 1/(0.0065)

def convertPackage(packet : serialParser.RocketData):
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
        Gps_altitude : float = 0
        timestamp : float = 0
        localtime : string %H:%M:%S
        altitude: float in meters
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
    date = str(datetime.now())
    localtime = date[11:]
    results = [localtime] + results
    filePath = './data/Data_' + date[:10] + '.csv'
    header = []
    if not os.path.exists(filePath):
        #write header
        header += [
            'local time',
            'transmission timestamp',
            'Hts_temperature',
            'Lps_pressure',
            'Imu_accelX',
            'Imu_accelY',
            'Imu_accelZ',
            'Imu_gyroX',
            'Imu_gyroY',
            'Imu_gyroZ',
            'Imu_magX',
            'Imu_magY',
            'Imu_magZ',
            'Gps_lat',
            'Gps_lng',
            'Gps_altitude',
            'altitude'
        ]
    
    with open(filePath, 'a') as recordFile:
        writer = csv.writer(recordFile)
        if len(header) != 0:
            writer.writerow(header)
        writer.writerow(results)
    return results

    

