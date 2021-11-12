from enum import Enum, auto

class SensorState(Enum):
    IDLE = auto()
    TRIGGERED = auto()
    ACTIVE = auto()

class UltrasonicDistanceSensor:
    def __init__(self, startOffset, endOffset, state) -> None:
        self.__detectedDistance = 0
        self.__startOffset = startOffset
        self.__endOffset = endOffset
        self.__inRange = False
        self.__state = state

    def __updateState(self):
        if self.__state == SensorState.IDLE:
            if self.__inRange == True:    # IDLE -> TRIGGERED
                self.__state = SensorState.TRIGGERED
        elif self.__state == SensorState.TRIGGERED:
            if self.__inRange == True:    # TRIGGERED -> ACTIVE
                self.__state = SensorState.ACTIVE
            else:                       # TRIGGERED -> IDLE
                self.__state = SensorState.IDLE
        elif self.__state == SensorState.ACTIVE:
            if self.__inRange == False:   # ACTIVE -> IDLE
                self.__state = SensorState.IDLE


    def update(self, distance):
        self.__detectedDistance = distance

        if self.__startOffset < distance and self.__endOffset > distance:
            self.__inRange = True
        else:
            self.__inRange = False

        self.__updateState()

    def getDetectedDistance(self):
        return self.__detectedDistance

    def getState(self):
        return self.__state