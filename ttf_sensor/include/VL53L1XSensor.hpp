#ifndef VL53L1X_SENSOR
#define VL53L1X_SENSOR

#include "ITTFSensor.hpp"
#include "TTFSensorConfiguration.hpp"

class VL53L1XSensor : public ITTFSensor {
    private:
    //std::unique_ptr<TTFSensorConfiguration> config;

    public:
    VL53L1XSensor(int pin, int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange);
    float getDistance();
};

#endif // VL53L1X_SENSOR