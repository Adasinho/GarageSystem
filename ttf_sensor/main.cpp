#include <iostream>
#include <memory>
#include <string>

#include "Utils.hpp"
#include "ServerConfiguration.hpp"
#include "TTFSensorServer.hpp"

int main(int argc, char** argv) {
    if (argc < 1)
    {
        printf("This program needed path to configuration file\n");
        return 1;
    }

    std::string configFilePath = argv[1];
    nlohmann::json data = Utils::getJsonData(configFilePath);
    ServerConfiguiration config(data);

    std::unique_ptr<TTFSensorServer> server = std::make_unique<TTFSensorServer>(config.getIP(), config.getPort());
    server->runServer();

    return 0;
}
