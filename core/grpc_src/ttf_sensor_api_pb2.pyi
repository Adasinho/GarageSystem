from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TTFSensorId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_TTF_SENSOR_ID: _ClassVar[TTFSensorId]
    GATE_A_PARKING_TTF_SENSOR_ID: _ClassVar[TTFSensorId]
    GATE_A_POSITION_TTF_SENSOR_ID: _ClassVar[TTFSensorId]
    GATE_B_PARKING_TTF_SENSOR_ID: _ClassVar[TTFSensorId]
    GATE_B_POSITION_TTF_SENSOR_ID: _ClassVar[TTFSensorId]
UNKNOWN_TTF_SENSOR_ID: TTFSensorId
GATE_A_PARKING_TTF_SENSOR_ID: TTFSensorId
GATE_A_POSITION_TTF_SENSOR_ID: TTFSensorId
GATE_B_PARKING_TTF_SENSOR_ID: TTFSensorId
GATE_B_POSITION_TTF_SENSOR_ID: TTFSensorId

class MeasureRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: TTFSensorId
    def __init__(self, id: _Optional[_Union[TTFSensorId, str]] = ...) -> None: ...

class MeasureResponse(_message.Message):
    __slots__ = ("distance",)
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    distance: int
    def __init__(self, distance: _Optional[int] = ...) -> None: ...
