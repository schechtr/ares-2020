#pragma once
#include "RocketModule.h"

namespace Analog {
    uint16_t &CC = Rocket::data.Analog_CC;
    uint16_t &fuel = Rocket::data.Analog_fuel;
    uint16_t &OX = Rocket::data.Analog_OX;
    uint16_t &press = Rocket::data.Analog_press;

    class Handler: public Rocket::RocketModule {
    public:

        virtual bool warmup() {
            
            return true;
        }
        virtual void refresh() {

            CC = (analogRead(A0));
            fuel = (analogRead(A1));
            OX = (analogRead(A2));
            press = (analogRead(A3));

        }
    };
}