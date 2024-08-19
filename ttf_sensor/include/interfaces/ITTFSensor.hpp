#ifndef ITTF_SENSOR
#define ITTF_SENSOR

#include "TTFSensorConfiguration.hpp"
#include "Helpers.hpp"
#include "Exceptions.hpp"

class ITTFSensor {
    protected:
    std::unique_ptr<TTFSensorConfiguration> config;

    ITTFSensor(int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange)
    {
        if(shutdownPin < 0) throw TTFSensorConfigurationException("Shutdown pin number must be grater than 0");
        if(!Helpers::isCorrectTTFSensorId(id)) throw TTFSensorConfigurationException("Unknown sensor id");

        this->config = std::make_unique<TTFSensorConfiguration>(shutdownPin, address, id, minRange, maxRange);
    }

    public:
    virtual float getDistance() = 0;
};

#endif // ITTF_SENSOR