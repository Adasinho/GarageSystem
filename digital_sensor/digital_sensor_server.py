import grpc

from concurrent import futures

from grpc_src.digital_sensor_api_pb2_grpc import add_DigitalSensorServicer_to_server
from digital_sensor_servicer import DigitalSensorServicer


class DigitalSensorServer:
    def __init__(self, ip: str, port: str) -> None:
        self.ip = ip
        self.port = port
        
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        add_DigitalSensorServicer_to_server(DigitalSensorServicer(), self.server)
        
    def start(self) -> None:
        insecure_port = f"[{self.ip}]:{self.port}"
        self.server.add_insecure_port(insecure_port)
        print(f"Start listening on {insecure_port}")
        
        self.server.start()
        
    def wait_for_termination(self) -> None:
        self.server.wait_for_termination()