#include "RocketModule.h"
#include "rocket.h"

bool isOn = true;

void preWarmup();
void warmup();
void refresh();
void shutdown();

uint8_t enabledByte = 0xff;

bool byteFlag(uint8_t b, int idx) {
    return b & (1 << (7 - idx));
}

void setup() {
	Serial.begin(115200);
	uint32_t serialAwaitStart = millis();
	while(millis() - serialAwaitStart < 3000 && !Serial);
	Serial.println("Congratulations on your code compiling");
	preWarmup();
	warmup();
	Serial.println("Flushing remaining bytes");
	uint32_t flushStart = millis();
	while(millis() - flushStart < 2000 && Serial.read() > 0);
	pinMode(LED_BUILTIN, OUTPUT);
	Serial.println("Setup function complete, beginning telemetry");
}


uint32_t totalRefresh = 0;
bool highLoop = true;
void loop() {
	if(isOn) {
		if(highLoop) {
			digitalWrite(LED_BUILTIN, HIGH);
		}
		else {
			digitalWrite(LED_BUILTIN, LOW);
		}
		refresh();
		highLoop = !highLoop;
	}
	else {
		digitalWrite(LED_BUILTIN, LOW);
	}
}


/* generic implementations */
void preWarmup() {
    for(int i = 0; i < Rocket::MODULE_NUM; i++) {
       
        Serial.print("Pre-warming module: ");
        //Serial.println(Rocket::MODULE_NAMES[i]);
        Rocket::handlers[i]->preWarmup();
    }
    Serial.println("Pre-warmup complete");
}

void warmup() {
    for(int i = 0; i < Rocket::MODULE_NUM ; i++) {
       
        Serial.print("Warming up: ");
        //Serial.println(Rocket::MODULE_NAMES[i]);
        if(Rocket::handlers[i]->warmup()) {
            Serial.println(" ...successful");
            
        }
        else {
            Serial.println(" ...unsuccessful, disabling");
            enabledByte &= ~(1 << (7 - i));
        }
    }
    Serial.println("Warmup complete");
}

void refresh() {
    for(int i = 0; i < Rocket::MODULE_NUM; i++) {
        if(!byteFlag(enabledByte, i)) {
            continue;
        }
        //Serial.print("Refreshing: ");
        //Serial.println(Rocket::MODULE_NAMES[i]);
        Rocket::handlers[i]->refresh();
        
        Rocket::data.timestamp = millis(); //update timestamp
    }
}

void shutdown() {
    for(int i = 0; i < Rocket::MODULE_NUM; i++) {
        if(!byteFlag(enabledByte, i)) {
            continue;
        }
        Serial.print(F("Shutting down: "));
        //Serial.println(Rocket::MODULE_NAMES[i]);
        Rocket::handlers[i]->shutdown();
    }
    Serial.println(F("Shut down. Goodbye!"));
}