#include <iostream>
#include <memory>
#include <string>

#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>

#include "grpc_src/ttf_sensor_api.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;

using ttf_sensor_api::TTFSensorService;
using ttf_sensor_api::Measure;
using ttf_sensor_api::MeasureResponse;

// Implementacja serwisu
class TTFSensorServiceImpl final : public TTFSensorService::Service {
 public:
  Status GetMeasure(ServerContext* context, const Measure* request,
                         MeasureResponse* reply) override {
    std::int32_t distance = request->distance();
    std::cout << "Otrzymano żądanie pomiaru: " << distance << std::endl;

    // Tutaj umieść logikę odczytu stanu czujnika
    bool sensor_status = true;  // Przykładowy stan czujnika

    reply->set_success(sensor_status);
    return Status::OK;
  }
};

void RunServer() {
  std::string server_address("0.0.0.0:50052");  // Adres i port serwera
  TTFSensorServiceImpl service;

  grpc::EnableDefaultHealthCheckService(true);
  ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<Server> server(builder.BuildAndStart());
  std::cout << "Serwer działa na adresie: " << server_address << std::endl;
  server->Wait();
}

int main(int argc, char** argv) {
  RunServer();
  return 0;
}
