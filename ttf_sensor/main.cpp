#include <iostream>
#include <memory>
#include <string>

#include "Utils.hpp"
#include "ServerConfiguration.hpp"
#include "TTFSensorServer.hpp"
#include "TTFSensorsController.hpp"

int main(int argc, char** argv) {
    if (argc < 1)
    {
        printf("This program needed path to configuration file\n");
        return 1;
    }

    std::string configFilePath = argv[1];
    nlohmann::json data = Utils::getJsonData(configFilePath);
    std::unique_ptr<ServerConfiguration> config = std::make_unique<ServerConfiguration>(data);
    std::unique_ptr<TTFSensorsController> sensorsController = std::make_unique<TTFSensorsController>(configFilePath);
    std::unique_ptr<TTFProject::TTFSensorServer> server = std::make_unique<TTFProject::TTFSensorServer>(config.get(), sensorsController.get());
    server->runServer();

    return 0;
}
