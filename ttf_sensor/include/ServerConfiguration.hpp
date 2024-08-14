#ifndef SERVER_CONFIGURATION_HPP
#define SERVER_CONFIGURATION_HPP

#include "nlohmann/json.hpp"

using json = nlohmann::json;

class ServerConfiguration
{
    private:
    std::string ip;
    std::string port;

    public:
    ServerConfiguration(json configData);

    std::string getIP();
    std::string getPort();
};

#endif // SERVER_CONFIGURATION_HPP