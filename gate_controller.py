from gate_manager import GateManager
from magnectic_switch_controller import MagneticSwitchController
from digital_sensor_controller import DigitalSensorController
from ultrasonic_sensor_controller import UltrasonicSensorController
from time_to_flight_sensor_controller import TimeToFlightSensorController
from animation_controller import AnimationController

class GateController:
    def __init__(self, downTimeToFlightController: TimeToFlightSensorController, upTimeToFlightController: TimeToFlightSensorController,
                digitalSensorController: DigitalSensorController, closeMagneticSwitchController: MagneticSwitchController,
                openMagneticSwitchController: MagneticSwitchController, animationController: AnimationController):
        self.__downTimeToFlightController = downTimeToFlightController
        self.__upTimeToFlightController = upTimeToFlightController
        self.__digitalSensorController = digitalSensorController
        self.__closeMagneticSwitchController = closeMagneticSwitchController
        self.__openMagneticSwitchController = openMagneticSwitchController

        self.__gateManager = GateManager(downTimeToFlightController.getSensor(),
                                         upTimeToFlightController.getSensor(),
                                         digitalSensorController.getSensor(),
                                         closeMagneticSwitchController.getSensor(),
                                         openMagneticSwitchController.getSensor(),
                                         animationController.getManager())

    def update(self):
        self.__downTimeToFlightController.update()
        self.__upTimeToFlightController.update()
        self.__digitalSensorController.update()
        self.__closeMagneticSwitchController.update()
        self.__openMagneticSwitchController.update()

        self.__gateManager.update()

    def getCarState(self):
        return self.__gateManager.getCarState()