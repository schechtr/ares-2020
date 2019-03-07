#include "rocket.h"
#include "RocketModule.h"
///https://github.com/adafruit/Adafruit_BNO055/archive/master.zip
///https://github.com/adafruit/Adafruit_Sensor/archive/master.zip
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>

namespace BNO {
    float &w = Rocket::data.BNO_w;
    float &x = Rocket::data.BNO_x;
    float &y = Rocket::data.BNO_y;
    float &z = Rocket::data.BNO_z;

    Adafruit_BNO055 bno = Adafruit_BNO055(55);
    imu::Quaternion quat;

    class BnoModule: public Rocket::RocketModule {
    public:
        virtual bool warmup() {
            bool setupRight = bno.begin();
            if(!setupRight) {
                return false;
            }
            delay(100);
            bno.setExtCrystalUse(true);
            return true;
        }
        virtual void refresh() {
            quat = bno.getQuat();
	        w = quat.w();
    	    x = quat.x();
	        y = quat.y();
	        z = quat.z();
        }
    };
    BnoModule module;
    Rocket::RocketModule *handler = &module;
}