#pragma once
#include "RocketModule.h"
#include <Arduino_LPS22HB.h>

namespace Lps {

    float &pressure = Rocket::data.Lps_pressure;

    class Handler: public Rocket::RocketModule {
    public:
      
        virtual bool warmup() {
            bool setupRight = BARO.begin();
            if(!setupRight) {
                return false;
            }
            return setupRight;
        }
        virtual void refresh() {
            pressure = BARO.readPressure();
        }
        virtual void shutdown(){
            BARO.end();
        }
    };
}