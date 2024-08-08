#include "TTFSensorServer.hpp"

TTFSensorServer::TTFSensorServer(std::string ip, std::string port)
{
    this->ip = ip;
    this->port = port;
    this->address = "[" + ip + "]" + ":" + port; // must be different for IPv4 and Ipv6

    grpc::EnableDefaultHealthCheckService(true);
    
    this->builder.AddListeningPort(this->address, grpc::InsecureServerCredentials());
    this->builder.RegisterService(&this->service);
}

void TTFSensorServer::runServer()
{
    this->server = std::move(this->builder.BuildAndStart());
    std::cout << "Serwer działa na adresie: " << this->address << std::endl;
    this->server->Wait();
}
