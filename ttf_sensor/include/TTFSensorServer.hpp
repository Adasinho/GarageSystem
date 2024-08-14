#ifndef TTF_SENSOR_SERVER_HPP
#define TTF_SENSOR_SERVER_HPP

#include <string>

#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>

#include "TTFSensorServicer.hpp"

using grpc::Server;
using grpc::ServerBuilder;

//class TTFSensorServicer;
class ServerConfiguration;
class TTFSensorsController;

namespace TTFProject {
    class TTFSensorServer
    {
        private:
        std::string address;

        ServerBuilder builder;
        std::unique_ptr<Server> server;
        std::unique_ptr<TTFSensorServicer> service;

        TTFSensorsController* sensorsController;
        ServerConfiguration* config;

        public:
        TTFSensorServer(ServerConfiguration* config, TTFSensorsController* sensorsController);
        void runServer();
    };
}

#endif // TTF_SENSOR_SERVER_HPP