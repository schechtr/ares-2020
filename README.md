# ARES-TELEMETRY-2020

## Firmware Todo List
* choose a chipselcect pin for the bodytube system
* benchmark refresh times and optimize if necessary
* ~~test SD~~ works
* update bytes_per_refresh in radio.h based on how many bytes per second the radio is configured for
* timeout for warmups perhaps?
* ~~convert pressures to altitude~~ **moved to ground station**
* refresh scheduling

## Additional Info
* data is little endian


## About
This project is an Arduino sketch designed for the Nano 33 BLE that takes telemetry data from:
* pressure transducers
* IMU (Accelerometer,Gyro,Magnetometer) - LSM9DS1
* LPS (Barometer) - LPS22HB
* HTS (Temperature) - HTS221

and outputs it to:
* SD card
* RFD900 Radio

In 'firmware/', is the actual C++ code that is compiled and deployed to the device

### IMU on the Arduino NANO 33 BLE Sense

The IMU is a LSM9DS1, it is a 3-axis accelerometer, 3-axis gyroscope and 3-axis magnetometer. This chip, made by ST Microelectronics, is a standard component supported by the ArduinoLSM9DS1 library.


### Pressure on the Arduino NANO 33 BLE Sense

The barometer sensor is a LPS22HB, is an ultra-compact sensor which functions as a digital output barometer. This chip, made by ST is supported by the ArduinoLPS22HB library.

### Relative humidity and temperature on the Arduino NANO 33 BLE Sense

The relative humidity and temperature sensor is a HTS221, is an ultra-compact sensor that uses a polymer dielectric planar capacitor structure capable of detecting relative humidity variations and temperature, returned as digital output on a serial interface. This chip, made by ST is supported by the ArduinoHTS221 library.



