#pragma once

namespace Rocket {
	constexpr char* NAME_CSV = "Hts_temperature,Lps_pressure,Imu_accelX,Imu_accelY,Imu_accelZ,Imu_gyroX,Imu_gyroY,Imu_gyroZ,Imu_magX,Imu_magY,Imu_magZ,Gps_lat,Gps_lng,timestamp";
	constexpr char* TYPE_CSV = "float,float,float,float,float,float,float,float,float,float,float,float,float,uint32_t";
	constexpr char* MODULE_CSV = "Hts,Lps,Imu,Gps,Radio,SdCard";
	constexpr char* Hts_TEXT = "Hts";
    constexpr char* Lps_TEXT = "Lps";
	constexpr char* Imu_TEXT = "Imu";
    constexpr char* Gps_TEXT = "Gps";
	constexpr char* Radio_TEXT = "Radio";
	constexpr char* SdCard_TEXT = "SdCard";
	constexpr char* MODULE_NAMES[MODULE_NUM] = {
		Hts_TEXT,
        Lps_TEXT,
        Imu_TEXT,
		Gps_TEXT,
		Radio_TEXT,
		SdCard_TEXT
	};
}
