from grpc import ServicerContext

from grpc_src.digital_sensor_api_pb2 import StatusResponse, StatusRequest, SensorId
import digital_sensor_api_pb2_grpc

class DigitalSensorServicer(digital_sensor_api_pb2_grpc.DigitalSensorServicer):
    def GetStatus(self, request: StatusRequest, context: ServicerContext) -> StatusResponse:
        print(f"Get request for {request.id} sensor")
        
        success = request.id == SensorId.GATE_A_PRESENCE_SENSOR_ID
        response = StatusResponse(success=success)
        
        return response