#include <string>

#include "TTFSensorServiceImpl.hpp"

#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>

using grpc::Server;
using grpc::ServerBuilder;

class TTFSensorServer
{
    private:
    std::string ip;
    std::string port;
    std::string address;

    ServerBuilder builder;
    std::unique_ptr<Server> server;
    TTFSensorServiceImpl service;

    public:
    TTFSensorServer(std::string ip, std::string port);
    void runServer();
};