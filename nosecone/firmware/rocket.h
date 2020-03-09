#pragma once

#include "RocketModule.h"

namespace Rocket {
	#pragma pack(push, 1)
	struct ROCKET_DATA {
		uint8_t start1 = 0xff;
		uint8_t start2 = 0xff;
		uint32_t timestamp;
		float Hts_temperature;
		float Lps_pressure;
		float Imu_accelX;
		float Imu_accelY;
		float Imu_accelZ;
		float Imu_gyroX;
		float Imu_gyroY;
		float Imu_gyroZ;
		float Imu_magX;
		float Imu_magY;
		float Imu_magZ;
        float Gps_lat;
        float Gps_lng;
        float Gps_altitude;
		uint8_t end1 = 0xA4;
		uint8_t end2 = 0x55;
	};
	#pragma pack(pop)
	static ROCKET_DATA data;

	const char *DATA_START = (char *)&data;
	const int DATA_LEN = sizeof(ROCKET_DATA);

	const int MODULE_NUM = 6;
	const int Hts_ID = 0;
	const int Lps_ID = 1;
	const int Imu_ID = 2;
    const int Gps_ID = 3;
	const int Radio_ID = 4;
	const int SdCard_ID = 5;
}

#include "rocket_strings.h"
#include "Hts.h"
#include "Lps.h"
#include "Imu.h"
#include "Gps.h"
#include "Radio.h"
#include "SdCard.h"

namespace Rocket {
	static Hts::Handler Hts_INSTANCE;
    static Lps::Handler Lps_INSTANCE;
	static Imu::Handler Imu_INSTANCE;
    static Gps::Handler Gps_INSTANCE;
	static Radio::Handler Radio_INSTANCE;
	static SdCard::Handler SdCard_INSTANCE;
	static RocketModule *handlers[] = {&Hts_INSTANCE, &Lps_INSTANCE, &Imu_INSTANCE, &Gps_INSTANCE, 
                                       &Radio_INSTANCE, &SdCard_INSTANCE};
}
