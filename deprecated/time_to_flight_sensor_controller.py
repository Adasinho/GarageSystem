from adafruit_blinka.microcontroller.bcm283x.pin import Pin
from ultrasonic_distance_sensor import UltrasonicDistanceSensor, SensorState
from dataclasses import dataclass

import adafruit_vl53l0x
import VL53L1X
import busio
import board

@dataclass
class TimeToFlightSensorParams:
    rangeMin: int
    rangeMax: int
    name: str
    address: hex
    xshutPin: Pin

class TimeToFlightSensorController:
    def __init__(self, config: TimeToFlightSensorParams) -> None:
        self.__sensorName = config.name
        self.__i2c = busio.I2C(board.SCL, board.SDA)
        self.__sensor = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=config.address)
        self.__sensor.open()

        distance = self.__readData()
        state = SensorState.ACTIVE if config.rangeMin < distance and config.rangeMax > distance else SensorState.IDLE

        self.__ultrasonicDistanceSensor = UltrasonicDistanceSensor(config.rangeMin, config.rangeMax, state)

    def __readData(self):
        self.__sensor.start_ranging(1)
        value = self.__sensor.get_distance() / 10
        self.__sensor.stop_ranging()
        return value
    
    def update(self):
        distance = self.__readData()
        ### print("[" + self.__sensorName + "] distance: {}".format(distance))
        self.__ultrasonicDistanceSensor.update(distance)

    def getSensor(self):
        return self.__ultrasonicDistanceSensor