import grpc
import sys
import os

# Fix problem with directories
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'grpc_src'))

from grpc_src import digital_sensor_api_pb2
from grpc_src import ttf_sensor_api_pb2

from digital_sensor_client import DigitalSensorClient
from ttf_sensor_client import TTFSensorClient

from utils import get_json_data

# Load configuration file
data = get_json_data("../configuration.json")
DIGITAL_SENSOR_SERVER_IP = data["digital_sensor_service"]["address_ip"]
DIGITAL_SENSOR_SERVER_PORT = data["digital_sensor_service"]["port"]

TTF_SENSOR_SERVER_IP = data["ttf_sensor_service"]["address_ip"]
TFF_SENSOR_SERVER_PORT = data["ttf_sensor_service"]["port"]

def main():
    digital_service_client = DigitalSensorClient(DIGITAL_SENSOR_SERVER_IP, DIGITAL_SENSOR_SERVER_PORT)
    sensor_status = digital_service_client.get_status(digital_sensor_api_pb2.SensorId.GATE_A_PRESENCE_SENSOR_ID)
    
    ttf_sensor_client = TTFSensorClient(TTF_SENSOR_SERVER_IP, TFF_SENSOR_SERVER_PORT)
    distance = ttf_sensor_client.get_distance(ttf_sensor_api_pb2.TTFSensorId.GATE_A_PARKING_TTF_SENSOR_ID)
    
    if sensor_status:
        print("Wywołanie GetStatus zakończone pomyślnie")
    else:
        print("Wywołanie GetStatus zakończone niepowodzeniem")
        
if __name__ == "__main__":
    main()
        