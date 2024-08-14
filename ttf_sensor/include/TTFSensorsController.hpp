#ifndef TTF_SENSORS_CONTROLLER_HPP
#define TTF_SENSORS_CONTROLLER_HPP

#include <string>
#include <vector>
#include <memory>

#include "ITTFSensor.hpp"

class TTFSensorsController {
    private:
    std::vector<std::unique_ptr<ITTFSensor>> sensors;

    public:
    TTFSensorsController(std::string configFilePath);
};

#endif // TTF_SENSORS_CONTROLLER_HPP