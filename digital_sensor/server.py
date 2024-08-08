from digital_sensor_server import DigitalSensorServer

from utils import get_json_data

def serve():
    # Load configuration file
    data = get_json_data("../configuration.json")
    DIGITAL_SENSOR_SERVICE_IP = data["digital_sensor_service"]["address_ip"]
    DIGITAL_SENSOR_SERVICE_PORT = data["digital_sensor_service"]["port"]
    
    server = DigitalSensorServer(DIGITAL_SENSOR_SERVICE_IP, DIGITAL_SENSOR_SERVICE_PORT)
    server.start()
    server.wait_for_termination()
        
if __name__ == "__main__":
    serve()