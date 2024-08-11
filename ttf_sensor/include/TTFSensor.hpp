#include "TTFSensorConfiguration.hpp"

class TTFSensor {
    private:
    std::unique_ptr<TTFSensorConfiguration> config;

    public:
    TTFSensor(int pin, int shutdownPin, int address, TTFSensorId id, float minRange, float maxRange);
    float getDistance();
};