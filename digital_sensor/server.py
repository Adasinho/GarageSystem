import grpc
#import time
import sys
import os

# Fix problem with directories
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'grpc_src'))

from grpc_src import digital_sensor_api_pb2
from grpc_src import digital_sensor_api_pb2_grpc

from concurrent import futures

class DigitalSensorServiceServicer(digital_sensor_api_pb2_grpc.DigitalSensorServiceServicer):
    def GetStatus(self, request, context):
        response = digital_sensor_api_pb2.StatusResponse()
        response.success = request.id == digital_sensor_api_pb2.SensorId.GATE_PRESENCE_SENSOR_ID
        return response
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    digital_sensor_api_pb2_grpc.add_DigitalSensorServiceServicer_to_server(DigitalSensorServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    
    print("Start listening on [::]:50051")
    
    server.start()
    server.wait_for_termination()
    
    #print("Server running on port 50051")
    #try:
    #    while True:
    #        time.sleep(86400)
    #except KeyboardInterrupt:
    #    server.stop(0)
        
if __name__ == "__main__":
    serve()