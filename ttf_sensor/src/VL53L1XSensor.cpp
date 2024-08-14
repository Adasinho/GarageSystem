#include "VL53L1XSensor.hpp"

//#include "Helpers.hpp"

VL53L1XSensor::VL53L1XSensor(int pin, int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange)
    : ITTFSensor(pin, shutdownPin, address, id, minRange, maxRange) {}

float VL53L1XSensor::getDistance()
{
    return 0.0f;
}
