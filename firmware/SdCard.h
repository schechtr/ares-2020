#pragma once
#include <SD.h>
#include "RocketModule.h"

#define SD_CHIPSEL 9


namespace SdCard {
    class Handler : public Rocket::RocketModule {
    private:
        int bytesWritten = 0;
        const char *fileName = "rocket_data.bin";
        SDLib::File saveFile;

    public:
        virtual bool warmup() {
            if (!SD.begin(SD_CHIPSEL)) {
                Serial.println("SD initialization failed");
                return false;
            }
            Serial.print("Trying to create file: ");
            if (saveFile = SD.open(fileName, FILE_WRITE)) {
                Serial.println("Created file");
                return true;
            } else {
                Serial.println("Could not create file.");
                return false;
            }
            Serial.println("all good");
            return true;
        }
        virtual void refresh() {
            // Remainder will store how many bytes overflow
            // Assume max size is 8 bytes, data len is 3, bytes written is 7
            int remainder = bytesWritten + Rocket::DATA_LEN - 512;  // 2
            remainder = max(0, remainder);                          // 2
            int k = saveFile.write(Rocket::DATA_START);  // writes [data+0, 1)

            if (bytesWritten + Rocket::DATA_LEN >= 512) {  // if 7 + 3 >= 8 (true)
                //int startMillis = millis();
                saveFile.close();  // flush
                saveFile = SD.open(fileName, FILE_WRITE);
                bytesWritten = remainder;
                if (bytesWritten > 0) {  // true
                    k += saveFile.write(
                        Rocket::DATA_START + Rocket::DATA_LEN - remainder,
                        remainder);  // writes [data+2, 6)
                }                    // 4

            } else {
                bytesWritten += Rocket::DATA_LEN;
            }
        }
        virtual void shutdown() { 
            saveFile.close(); 
        }
    }; 
}  // namespace SdCard