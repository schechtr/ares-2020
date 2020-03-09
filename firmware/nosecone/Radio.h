#pragma once
#include "RocketModule.h"

#define RADIO_BAUD 57600

namespace Radio {
    //configured for the razor imu
    class Handler: public Rocket::RocketModule {
    public:
        const int BYTES_PER_REFRESH = 30;
        bool needsRefresh = true;
        Rocket::ROCKET_DATA cache;
        int currentWrite = 0;
        char *cachePtr;
        virtual bool warmup() {
            //it's all RX TX, we can only hope
            Serial1.begin(RADIO_BAUD);
            cachePtr = (char *)&cache;
            return true;
        }
        virtual void refresh() {
            /*
            each "refresh", it'll send up to BYTES_PER_REFRESH bytes
            This will mean the data is stale, so it sets "needsRefresh" to high once its done writing a message
            Needs refresh copies a cached version of the struct and sends that
            
            Pro:
                Hella HZ
            Con:
                Radio is always stale
            */
            if(needsRefresh) {
                cache = Rocket::data;
                currentWrite = 0;
                needsRefresh = false;
            }
            int i = 0;
            while(i < BYTES_PER_REFRESH && currentWrite < Rocket::DATA_LEN) {
                Serial1.write(cachePtr[currentWrite]);
                i++;
                currentWrite++;
            }
            if(currentWrite >= Rocket::DATA_LEN) {
                needsRefresh = true;
            }
        }
    };
}