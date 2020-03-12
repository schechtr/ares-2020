#pragma once

namespace Rocket {
    // these arent being used anymore
	constexpr char* NAME_CSV = "Hts_temperature,Lps_pressure,Imu_accelX,Imu_accelY,Imu_accelZ,Imu_gyroX,Imu_gyroY,Imu_gyroZ,Imu_magX,Imu_magY,Imu_magZ,Gps_lat,Gps_lng,timestamp";
	constexpr char* TYPE_CSV = "float,float,float,float,float,float,float,float,float,float,float,float,float,uint32_t";
	constexpr char* MODULE_CSV = "Hts,Lps,Imu,Gps,Radio,SdCard";
    
    // these can be used in firmware.ino for debugging
	constexpr char* Hts_TEXT = "Hts";
    constexpr char* Lps_TEXT = "Lps";
	constexpr char* Imu_TEXT = "Imu";
    constexpr char* Analog_TEXT = "Analog";
	constexpr char* SdCard_TEXT = "SdCard";
	constexpr char* MODULE_NAMES[MODULE_NUM] = {
		Hts_TEXT,
        Lps_TEXT,
        Imu_TEXT,
		Analog_TEXT,
		SdCard_TEXT
	};
}
