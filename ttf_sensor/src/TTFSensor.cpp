#include "TTFSensor.hpp"

#include "Exceptions.hpp"
#include "Helpers.hpp"

TTFSensor::TTFSensor(int pin, int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange)
{
    if(pin < 0) throw TTFSensorConfigurationException("Pin number must be grater than 0");
    if(!Helpers::isCorrectTTFSensorId(id)) throw TTFSensorConfigurationException("Unknown sensor id");

    this->config = std::make_unique<TTFSensorConfiguration>(pin, shutdownPin, address, id, minRange, maxRange);
}

float TTFSensor::getDistance()
{
    return 0.0f;
}
