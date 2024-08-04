import grpc
import sys
import os

# Fix problem with directories
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'grpc_src'))

from grpc_src.digital_sensor_api_pb2 import SensorId
from grpc_src import ttf_sensor_api_pb2
from grpc_src import ttf_sensor_api_pb2_grpc

from utils import get_json_data

from digital_sensor_service_client import DigitalSensorServiceClient

# Load configuration file
data = get_json_data("../configuration.json")
DIGITAL_SENSOR_SERVICE_IP = data["digital_sensor_service"]["address_ip"]
DIGITAL_SENSOR_SERVICE_PORT = data["digital_sensor_service"]["port"]

TTF_SENSOR_A_SERVICE_IP = data["ttf_sensor_service_a"]["address_ip"]
TFF_SENSOR_A_SERVICE_PORT = data["ttf_sensor_service_a"]["port"]

#channel_digital_sensor = grpc.insecure_channel("[::]:50051")
channel_ttf_sensor = grpc.insecure_channel(f"[{TTF_SENSOR_A_SERVICE_IP}]:{TFF_SENSOR_A_SERVICE_PORT}")

#stub_digital_sensor = digital_sensor_api_pb2_grpc.DigitalSensorServiceStub(channel_digital_sensor)
stub_ttf_sensor =ttf_sensor_api_pb2_grpc.TTFSensorServiceStub(channel_ttf_sensor)

def main():
    digital_service_client = DigitalSensorServiceClient(DIGITAL_SENSOR_SERVICE_IP, DIGITAL_SENSOR_SERVICE_PORT)
    sensor_status = digital_service_client.get_status(SensorId.GATE_PRESENCE_SENSOR_ID)
    
    if sensor_status:
        print("Wywołanie GetStatus zakończone pomyślnie")
    else:
        print("Wywołanie GetStatus zakończone niepowodzeniem")
        
if __name__ == "__main__":
    main()
        