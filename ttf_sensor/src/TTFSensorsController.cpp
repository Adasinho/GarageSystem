#include "TTFSensorsController.hpp"

#include <string>

#include "Utils.hpp"
#include "Exceptions.hpp"
#include "Helpers.hpp"

#include "TTFSensorModel.hpp"
#include "TTFSensorFactory.hpp"

TTFSensorsController::TTFSensorsController(std::string configFilePath)
{
    json data = Utils::getJsonData(configFilePath);

    std::string sensors[4] = { "gate_a_parking_ttf_sensor", "gate_a_position_ttf_sensor", "gate_b_parking_ttf_sensor", "gate_b_position_ttf_sensor" };
    for(std::string sensorName : sensors)
    {
        try {
            //int pin = std::stoi(std::string(data["ttf_sensor_service"][sensorName]["pin"]));
            int shutdownPin = std::stoi(std::string(data["ttf_sensor_service"][sensorName]["shutdownPin"]));
            int address = std::stoi(std::string(data["ttf_sensor_service"][sensorName]["address"]));
            float minRange = std::stof(std::string(data["ttf_sensor_service"][sensorName]["minRange"]));
            float maxRange = std::stof(std::string(data["ttf_sensor_service"][sensorName]["maxRange"]));
            TTFSensorId id = Helpers::getTTFSensorIDFromName(sensorName);

            std::string type = std::string(data["ttf_sensor_service"][sensorName]["type"]);
            TTFSensorModel sensorModel = Helpers::getTTFSensorModelFromString(type);
            this->sensors.push_back(TTFSensorFactory::makeTTFSensor(sensorModel, shutdownPin, address, id, minRange, maxRange));
        } catch(const TTFSensorConfigurationException& e) {
            std::cerr << "Can not create TTFSensor: " << e.what() << std::endl;
        } catch(const TTFSensorInicializationException& e) {
            std::cerr << "Can not create TTFSensor: " << e.what() << std::endl;
        } catch(...) {
            std::cerr << "Can not create TTFSensor: Unknown error" << std::endl;
        }
        
    }

    // TODO: Loop over all sensors and disable it
    // TODO: Loop over all sensors and turn it with setting address
}