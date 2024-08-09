import grpc

from grpc_src import ttf_sensor_api_pb2_grpc
from grpc_src.ttf_sensor_api_pb2 import MeasureRequest, MeasureResponse, TTFSensorId

class TTFSensorClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        
        self.channel = grpc.insecure_channel(f"[{ip}]:{port}")
        self.stub = ttf_sensor_api_pb2_grpc.TTFSensorStub(self.channel)

    def get_distance(self, sensor_id: TTFSensorId):
        request = MeasureRequest(id=sensor_id)
        print(f"TTF SENSOR REQUEST ID: {request.id}")
        
        response: MeasureResponse = self.stub.GetMeasure(request)
        return response.distance