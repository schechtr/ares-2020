#pragma once
#include "RocketModule.h"
#include <TinyGPS++.h>

#define RX_GPS 10
#define TX_GPS 9
#define GPS_BAUD 9600

namespace Gps{
    float &lat = Rocket::data.Gps_lat;
    float &lng = Rocket::data.Gps_lng;
    
    UART gpsSerial(digitalPinToPinName(RX_GPS), digitalPinToPinName(TX_GPS), NC, NC);

    class Handler: public Rocket::RocketModule {
    public:

        TinyGPSPlus gps;

        virtual bool warmup() {
            gpsSerial.begin(GPS_BAUD);
           
            return true;
        }
        virtual void refresh() {
            long start = millis();
            while(gpsSerial.available() > 0 && millis() - start < 25) {
                if(gps.encode(gpsSerial.read())) {
                    if(gps.location.isValid()) {
                        lat = gps.location.lat();
                        lng = gps.location.lng();
                    }
                }
            }
            
        }
    };
}