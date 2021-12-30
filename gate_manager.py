from enum import Enum, auto
from animation import AnimationFrame, AnimationState

from ultrasonic_distance_sensor import UltrasonicDistanceSensor, SensorState as UltrasonicState
from digital_distance_sensor import DigitalDistanceSensor, SensorState as DigitalState
from magnetic_switch import MagneticSwitch
from animation_manager import AnimationManager
from animation_player import WHITE_COLOR

class GateState(Enum):
    CLOSED = auto()
    OPENED = auto()
    ON_MOVE = auto()

class CarState(Enum):
    PARKED = auto()
    ENTERING = auto()
    DEPARTING = auto()
    APART_FROM = auto()

RANGE_MIN = 0
RANGE_MAX = 100

class GateManager:
    def __init__(self, downTimeToFlightSensor: UltrasonicDistanceSensor, upTimeToFlightSensor: UltrasonicDistanceSensor,
                digitalSensor: DigitalDistanceSensor, closeMagneticSwitch: MagneticSwitch, openMagneticSwitch: MagneticSwitch,
                animationManager: AnimationManager) -> None:
        ### print("GATE MANAGER")
        self.__downTimeToFlightSensor = downTimeToFlightSensor
        self.__upTimeToFlightSensor = upTimeToFlightSensor
        self.__digitalSensor = digitalSensor
        self.__closeMagneticSwitch = closeMagneticSwitch
        self.__openMagneticSwitch = openMagneticSwitch
        #self.__gateState = GateState.CLOSED
        #self.__carState = CarState.PARKED
        self.__animationManager = animationManager
        self.__animationFrame = AnimationFrame(WHITE_COLOR, RANGE_MIN, RANGE_MAX)

        self.__updateGateState()
        self.__initSetting()
        ### print("END GATE MANAGER")

    def __initSetting(self):
        if self.__upTimeToFlightSensor.getState() == UltrasonicState.ACTIVE or self.__upTimeToFlightSensor.getState() == UltrasonicState.TRIGGERED:
            self.__carState = CarState.PARKED
        else:
            self.__carState = CarState.APART_FROM

    def __updateGateState(self):
        if self.__openMagneticSwitch.isActive():
            self.__gateState = GateState.OPENED
        elif self.__closeMagneticSwitch.isActive():
            self.__gateState = GateState.CLOSED
        else:
            self.__gateState = GateState.ON_MOVE
    
    def __updateCarState(self):
        ### print("self.__upTimeToFlightSensor.getState():", self.__upTimeToFlightSensor.getState())
        ### print("self.__digitalSensor.getState():", self.__digitalSensor.getState())
        if self.__carState == CarState.APART_FROM:
            if (self.__upTimeToFlightSensor.isActive() and self.__downTimeToFlightSensor.isActive() and not self.__digitalSensor.isActive()):
                self.__carState = CarState.ENTERING
                self.__animationFrame.rangeMin = self.__downTimeToFlightSensor.getDetectedDistance()
                self.__animationFrame.rangeMax = RANGE_MAX
                self.__animationManager.changeAnimation(AnimationState.RANGE)
        elif self.__carState == CarState.ENTERING:
            if self.__digitalSensor.isActive():
                ### print("Czary czary czary")
                self.__animationManager.restartAnimation()
            if (self.__upTimeToFlightSensor.isActive() and self.__downTimeToFlightSensor.isActive() and not self.__digitalSensor.isActive()):
                if self.__animationManager.isIdle():
                    self.__carState = CarState.PARKED
                    self.__animationFrame.newColor = WHITE_COLOR
                    self.__animationManager.changeAnimation(AnimationState.IDLE)
            elif not self.__digitalSensor.isActive():
                self.__carState = CarState.APART_FROM
                self.__animationFrame.newColor = WHITE_COLOR
                self.__animationManager.changeAnimation(AnimationState.IDLE)
        elif self.__carState == CarState.PARKED:
            if ((not self.__upTimeToFlightSensor.isActive()) and self.__downTimeToFlightSensor.isActive() and self.__digitalSensor.isActive()):
                self.__carState = CarState.DEPARTING
                self.__animationFrame.newColor = WHITE_COLOR
                self.__animationManager.changeAnimation(AnimationState.IDLE)
        elif self.__carState == CarState.DEPARTING:
            if (not self.__upTimeToFlightSensor.isActive() and not self.__downTimeToFlightSensor.isActive() and not self.__digitalSensor.isActive()):
                self.__carState = CarState.APART_FROM
                self.__animationFrame.newColor = WHITE_COLOR
                self.__animationManager.changeAnimation(AnimationState.IDLE)

    def update(self):
        self.__updateCarState()
        self.__updateGateState()
        self.__updateAnimationFrame()
        self.__animationManager.update()

    def getCarState(self):
        return self.__carState

    def __updateAnimationFrame(self):
        self.__animationFrame.value = self.__downTimeToFlightSensor.getDetectedDistance()
        self.__animationManager.updateFrame(self.__animationFrame)