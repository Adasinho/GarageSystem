from enum import Enum, auto

class SensorState(Enum):
    IDLE = auto()
    TRIGGERED = auto()
    ACTIVE = auto()

class DigitalDistanceSensor:
    def __init__(self, state) -> None:
        self.__detected = False
        self.__state = state

    def __updateState(self):
        if self.__state == SensorState.IDLE:
            if self.__detected:    # IDLE -> TRIGGERED
                self.__state = SensorState.TRIGGERED
        elif self.__state == SensorState.TRIGGERED:
            if self.__detected:    # TRIGGERED -> ACTIVE
                self.__state = SensorState.ACTIVE
            else:                       # TRIGGERED -> IDLE
                self.__state = SensorState.IDLE
        elif self.__state == SensorState.ACTIVE:
            if not self.__detected:   # ACTIVE -> IDLE
                self.__state = SensorState.IDLE

    def update(self, detected):

        if detected:
            self.__detected = True
        else:
            self.__detected = False

        self.__updateState()

    def getState(self):
        return self.__state
    
    def isActive(self):
        return self.__state == SensorState.TRIGGERED or self.__state == SensorState.ACTIVE