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
        print("GATE MANAGER")
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
        print("END GATE MANAGER")

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
        # upUltrasonic = ACTIVE, digital = IDLE
        print("self.__upTimeToFlightSensor.getState():", self.__upTimeToFlightSensor.getState())
        print("self.__digitalSensor.getState():", self.__digitalSensor.getState())
        if (((self.__upTimeToFlightSensor.getState() == UltrasonicState.ACTIVE) or (self.__upTimeToFlightSensor.getState() == UltrasonicState.TRIGGERED)) and 
           (self.__digitalSensor.getState() == DigitalState.IDLE) and
           ((self.__carState == CarState.APART_FROM) or (self.__carState == CarState.ENTERING))):
            if self.__animationManager.isIdle():
                self.__carState = CarState.PARKED
                self.__animationFrame.newColor = WHITE_COLOR
                self.__animationManager.changeAnimation(AnimationState.IDLE)
            else:
                self.__carState = CarState.ENTERING
                self.__animationFrame.rangeMin = self.__downTimeToFlightSensor.getDetectedDistance()
                self.__animationFrame.rangeMax = RANGE_MAX
                self.__animationManager.changeAnimation(AnimationState.RANGE)
        # upUltrasonic = IDLE, digital = ACTIVE
        elif ((self.__upTimeToFlightSensor.getState() == UltrasonicState.IDLE) and
             ((self.__digitalSensor.getState() == DigitalState.ACTIVE) or (self.__digitalSensor.getState() == DigitalState.TRIGGERED))):
            # carState = PARKED
            if self.__carState == CarState.PARKED:
                self.__carState = CarState.DEPARTING
                self.__animationFrame.newColor = WHITE_COLOR
                self.__animationManager.changeAnimation(AnimationState.IDLE)
            elif(self.__downTimeToFlightSensor.getState() == UltrasonicState.IDLE):
                # carState = APART_FROM
                if self.__carState == CarState.APART_FROM:
                    self.__carState = CarState.ENTERING
                    carDistance = self.__downTimeToFlightSensor.getDetectedDistance()
                    rangeMin = carDistance if carDistance < RANGE_MAX else RANGE_MIN
                    self.__animationFrame.rangeMin = rangeMin
                    self.__animationFrame.rangeMax = RANGE_MAX
                    self.__animationManager.changeAnimation(AnimationState.RANGE)
        
        # upUltrasonic = IDLE, digital = IDLE
        elif (self.__upTimeToFlightSensor.getState() == UltrasonicState.IDLE) and (self.__digitalSensor.getState() == DigitalState.IDLE):
            # carState = DEPARTING
            if self.__carState == CarState.DEPARTING:
                self.__carState = CarState.APART_FROM
                self.__animationFrame.newColor = WHITE_COLOR
                self.__animationManager.changeAnimation(AnimationState.IDLE)
        elif (self.__carState == CarState.ENTERING):
            if(self.__digitalSensor.getState() == DigitalState.ACTIVE or self.__digitalSensor.getState() == DigitalState.TRIGGERED):
                print("Czary czary czary")
                self.__animationManager.restartAnimation()

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