#ifndef TTF_SENSOR
#define TTF_SENSOR

#include "TTFSensorConfiguration.hpp"

class TTFSensor {
    private:
    std::unique_ptr<TTFSensorConfiguration> config;

    public:
    TTFSensor(int pin, int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange);
    float getDistance();
};

#endif // TTF_SENSOR