#include "TTFSensorConfiguration.hpp"
#include "Helpers.hpp"

TTFSensorConfiguration::TTFSensorConfiguration(int pin, int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange)
{
    this->pin = pin;
    this->shutdownPin = shutdownPin;
    this->address = address;
    this->id = id;
    this->minRange = minRange;
    this->maxRange = maxRange;

    this->name = Helpers::getTTFSensorIDName(id);
}

int TTFSensorConfiguration::getPin()
{
    return this->pin;
}

int TTFSensorConfiguration::getShutdownPin()
{
    return this->shutdownPin;
}

int TTFSensorConfiguration::getAddress()
{
    return this->address;
}

std::string TTFSensorConfiguration::getName()
{
    return this->name;
}
