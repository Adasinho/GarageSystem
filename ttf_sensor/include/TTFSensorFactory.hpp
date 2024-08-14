#ifndef TTF_SENSOR_FACTORY_HPP
#define TTF_SENSOR_FACTORY_HPP

#include <memory>

#include "TTFSensorModel.hpp"
#include "ITTFSensor.hpp"

class TTFSensorFactory {
    public:
    static std::unique_ptr<ITTFSensor> makeTTFSensor(
        TTFSensorModel sensorModel, int pin, int shutdownPin,
        int address, TTFSensorId id, float minRange, float maxRange
    );
};

#endif // TTF_SENSOR_FACTORY_HPP