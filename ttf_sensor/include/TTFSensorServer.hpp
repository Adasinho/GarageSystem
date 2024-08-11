#include <string>

#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>

#include "TTFSensorServicer.hpp"

using grpc::Server;
using grpc::ServerBuilder;

class TTFSensorsController;

namespace TTFProject {
    class TTFSensorServer
    {
        private:
        std::string ip;
        std::string port;
        std::string address;

        ServerBuilder builder;
        std::unique_ptr<Server> server;
        TTFSensorsController* sensorsController;
        std::unique_ptr<TTFSensorServicer> service;

        public:
        TTFSensorServer(std::string ip, std::string port, TTFSensorsController* sensorsController);
        void runServer();
    };
}