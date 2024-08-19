#include "TTFSensorFactory.hpp"

#include "VL53L1XSensor.hpp"

std::unique_ptr<ITTFSensor> TTFSensorFactory::makeTTFSensor(TTFSensorModel sensorModel, int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange)
{
    switch(sensorModel) {
        case TTFSensorModel::TTF_SENSOR_MODEL_VL53L1X:
            return std::make_unique<VL53L1XSensor>(shutdownPin, address, id, minRange, maxRange);
        default:
            return nullptr;
    }
}