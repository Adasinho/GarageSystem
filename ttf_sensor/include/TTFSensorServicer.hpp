#include <grpcpp/grpcpp.h>

#include "ttf_sensor_api.grpc.pb.h"

using grpc::ServerContext;
using grpc::Status;

//using ttf_sensor_api::TTFSensor;
using ttf_sensor_api::TTFSensorId;
using ttf_sensor_api::MeasureRequest;
using ttf_sensor_api::MeasureResponse;

class TTFSensorServicer final : public ttf_sensor_api::TTFSensor::Service {
  public:
    Status GetMeasure(ServerContext* context, const MeasureRequest* request,
                         MeasureResponse* reply) override;
};