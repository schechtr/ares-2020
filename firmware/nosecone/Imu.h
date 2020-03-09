#pragma once
#include "RocketModule.h"
#include <Arduino_LSM9DS1.h>

namespace Imu {
    
    float &accelX = Rocket::data.Imu_accelX;
    float &accelY = Rocket::data.Imu_accelY;
    float &accelZ = Rocket::data.Imu_accelZ;
    float &gyroX = Rocket::data.Imu_gyroX;
    float &gyroY = Rocket::data.Imu_gyroY;
    float &gyroZ = Rocket::data.Imu_gyroZ;
    float &magX = Rocket::data.Imu_magX;
    float &magY = Rocket::data.Imu_magY;
    float &magZ = Rocket::data.Imu_magZ;

    class Handler: public Rocket::RocketModule {
    public:
        virtual bool warmup() {
            bool setupRight = IMU.begin();
            if(!setupRight) {
                return false;
            }

            return setupRight;
        }
        virtual void refresh() {
            if (IMU.accelerationAvailable()) {
                IMU.readAcceleration(accelX, accelY, accelZ);
            }
            if (IMU.gyroscopeAvailable()) {
                IMU.readGyroscope(gyroX, gyroY, gyroZ);
            }
            if (IMU.magneticFieldAvailable()) {
                IMU.readMagneticField(magX, magY, magZ);
            }
        }
        virtual void shutdown() {
            IMU.end();
        }
    };

}