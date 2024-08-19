#include "TTFSensorConfiguration.hpp"
#include "Helpers.hpp"

TTFSensorConfiguration::TTFSensorConfiguration(int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange)
{
    this->shutdownPin = shutdownPin;
    this->address = address;
    this->id = id;
    this->minRange = minRange;
    this->maxRange = maxRange;

    this->name = Helpers::getTTFSensorIDName(id);
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
