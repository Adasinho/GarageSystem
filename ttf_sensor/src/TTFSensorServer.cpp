#include "TTFSensorServer.hpp"
#include "TTFSensorsController.hpp"
#include "ServerConfiguration.hpp"

TTFProject::TTFSensorServer::TTFSensorServer(ServerConfiguration* config, TTFSensorsController* sensorsController)
{
    this->address = "[" + config->getIP() + "]" + ":" + config->getPort(); // must be different for IPv4 and Ipv6

    grpc::EnableDefaultHealthCheckService(true);

    this->service = std::make_unique<TTFSensorServicer>();
    
    this->builder.AddListeningPort(this->address, grpc::InsecureServerCredentials());
    this->builder.RegisterService(this->service.get());

    this->sensorsController = sensorsController;
}

void TTFProject::TTFSensorServer::runServer()
{
    this->server = std::move(this->builder.BuildAndStart());
    std::cout << "Serwer działa na adresie: " << this->address << std::endl;
    this->server->Wait();
}
