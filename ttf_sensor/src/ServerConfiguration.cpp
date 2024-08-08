#include "ServerConfiguration.hpp"

ServerConfiguiration::ServerConfiguiration(json configData)
{
    this->ip = configData["ttf_sensor_service"]["address_ip"];
    this->port = configData["ttf_sensor_service"]["port"];
}

std::string ServerConfiguiration::getIP()
{
    return this->ip;
}

std::string ServerConfiguiration::getPort()
{
    return this->port;
}
