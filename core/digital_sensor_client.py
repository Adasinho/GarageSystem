import grpc

from grpc_src import digital_sensor_api_pb2_grpc

from grpc_src.digital_sensor_api_pb2 import SensorId, StatusRequest, StatusResponse

class DigitalSensorClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        
        self.channel = grpc.insecure_channel(f"[{ip}]:{port}")
        self.stub = digital_sensor_api_pb2_grpc.DigitalSensorStub(self.channel)
        
    def get_status(self, sensor_id: SensorId) -> bool:
        request = StatusRequest(id=sensor_id)
        print(f"REQUEST.ID: {request.id}")
        response: StatusResponse = self.stub.GetStatus(request)
        
        return response.success