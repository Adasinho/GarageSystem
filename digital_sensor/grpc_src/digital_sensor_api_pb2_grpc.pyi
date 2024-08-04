from _typeshed import Incomplete

GRPC_GENERATED_VERSION: str
GRPC_VERSION: Incomplete
EXPECTED_ERROR_RELEASE: str
SCHEDULED_RELEASE_DATE: str

class DigitalSensorServiceStub:
    GetStatus: Incomplete
    def __init__(self, channel) -> None: ...

class DigitalSensorServiceServicer:
    def GetStatus(self, request, context) -> None: ...

def add_DigitalSensorServiceServicer_to_server(servicer, server) -> None: ...

class DigitalSensorService:
    @staticmethod
    def GetStatus(request, target, options=..., channel_credentials: Incomplete | None = ..., call_credentials: Incomplete | None = ..., insecure: bool = ..., compression: Incomplete | None = ..., wait_for_ready: Incomplete | None = ..., timeout: Incomplete | None = ..., metadata: Incomplete | None = ...): ...
