#include "TTFSensorServer.hpp"
#include "TTFSensorsController.hpp"

TTFProject::TTFSensorServer::TTFSensorServer(std::string ip, std::string port, TTFSensorsController* sensorsController)
{
    this->ip = ip;
    this->port = port;
    this->address = "[" + ip + "]" + ":" + port; // must be different for IPv4 and Ipv6

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
