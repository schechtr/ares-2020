#pragma once
#include "RocketModule.h"
#include <TinyGPS++.h>

#define RX_GPS 9
#define TX_GPS 10
#define GPS_BAUD 9600

namespace Gps{
    float &lat = Rocket::data.Gps_lat;
    float &lng = Rocket::data.Gps_lng;
    
    UART gpsSerial(digitalPinToPinName(RX_GPS), digitalPinToPinName(TX_GPS), NC, NC);

    class Handler: public Rocket::RocketModule {
    public:

        TinyGPSPlus gps;

        virtual bool warmup() {
            bool setupRight = gpsSerial.begin(GPS_BAUD);
            if(!setupRight) {
                return false;
            }

            return setupRight;
        }
        virtual void refresh() {
            
            if(!gps.location.isUpdated()) {
                return;
            }

            lat = gps.location.lat();
            lng = gps.location.lng();   
        }
    };
}