#include "ServerConfiguration.hpp"

ServerConfiguration::ServerConfiguration(json configData)
{
    this->ip = configData["ttf_sensor_service"]["address_ip"];
    this->port = configData["ttf_sensor_service"]["port"];
}

std::string ServerConfiguration::getIP()
{
    return this->ip;
}

std::string ServerConfiguration::getPort()
{
    return this->port;
}
