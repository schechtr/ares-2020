#pragma once
#include <SPI.h>
#include <SD.h>
#include "RocketModule.h"

const int chipSelect = 3;


namespace SdCard {
    class Handler : public Rocket::RocketModule {

    private:
      File dataFile;
      char filename[13] = "Rocket_Data";

    public:
        virtual bool warmup() {

          if (!SD.begin(chipSelect)) {
            Serial.println("Card failed, or not present");
            // don't do anything more:
            while (1);
          }
          Serial.println("card initialized.");

          return true;
        }
        virtual void refresh() {
            
            dataFile = SD.open(filename, FILE_WRITE);
          
            // if the file is available, write to it:
            if (dataFile) {
              dataFile.write(Rocket::DATA_START, Rocket::DATA_LEN);
              dataFile.close();
            }
            else {
              Serial.println("error opening file");
            }
        }

        virtual void shutdown() { 
            dataFile.close(); 
        }
    }; 
}  
