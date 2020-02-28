#pragma once

#include "RocketModule.h"

namespace Rocket {
	#pragma pack(push, 1)
	struct ROCKET_DATA {
		byte start1 = 0xff;
		byte start2 = 0xff;
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
		uint32_t timestamp;
		byte end1 = 0xA4;
		byte end2 = 0x55;
	};
	#pragma pack(pop)
	static ROCKET_DATA data;

	const char *DATA_START = (char *)&data;
	const int DATA_LEN = sizeof(ROCKET_DATA);

	const int MODULE_NUM = 5;
	const int Analog_ID = 0;
	const int Bmp_ID = 1;
	const int Mpu_ID = 2;
	const int Radio_ID = 3;
	const int SdCard_ID = 4;
}

#include "rocket_strings.h"
#include "Analog.h"
#include "Bmp.h"
#include "Mpu.h"
#include "Radio.h"
#include "SdCard.h"

namespace Rocket {
	static Analog::Handler Analog_INSTANCE;
	static Bmp::Handler Bmp_INSTANCE;
	static Mpu::Handler Mpu_INSTANCE;
	static Radio::Handler Radio_INSTANCE;
	static SdCard::Handler SdCard_INSTANCE;
	static RocketModule *handlers[] = {&Analog_INSTANCE, &Bmp_INSTANCE, &Mpu_INSTANCE, &Radio_INSTANCE, &SdCard_INSTANCE};
}
