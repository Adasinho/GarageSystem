from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SensorId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_SENSOR_ID: _ClassVar[SensorId]
    GATE_PRESENCE_SENSOR_ID: _ClassVar[SensorId]
UNKNOWN_SENSOR_ID: SensorId
GATE_PRESENCE_SENSOR_ID: SensorId

class StatusRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: SensorId
    def __init__(self, id: _Optional[_Union[SensorId, str]] = ...) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
