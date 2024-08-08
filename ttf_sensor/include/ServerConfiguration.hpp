#include "nlohmann/json.hpp"

using json = nlohmann::json;

class ServerConfiguiration
{
    private:
    std::string ip;
    std::string port;

    public:
    ServerConfiguiration(json configData);

    std::string getIP();
    std::string getPort();
};