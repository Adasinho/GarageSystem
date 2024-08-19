#ifndef TTF_SENSOR_CONFIGURATION_HPP
#define TTF_SENSOR_CONFIGURATION_HPP

#include <string>

#include "ttf_sensor_api.grpc.pb.h"

using ttf_sensor_api::TTFSensorId;

class TTFSensorConfiguration {
private:
    int shutdownPin;
    int address;
    TTFSensorId id;
    std::string name;
    float minRange;
    float maxRange;

public:
    TTFSensorConfiguration(int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange);

    int getPin();
    int getShutdownPin();
    int getAddress();
    std::string getName();
};

#endif // TTF_SENSOR_CONFIGURATION_HPP