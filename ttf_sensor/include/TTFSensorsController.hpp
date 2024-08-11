#include <string>
#include <vector>
#include <memory>

#include "TTFSensor.hpp"

class TTFSensorsController {
    private:
    std::vector<std::unique_ptr<TTFSensor>> sensors;

    public:
    TTFSensorsController(std::string configFilePath);
};