from adafruit_blinka.microcontroller.bcm283x.pin import Pin
from ultrasonic_distance_sensor import UltrasonicDistanceSensor, SensorState
from dataclasses import dataclass

import adafruit_vl53l0x
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
        self.__sensor = adafruit_vl53l0x.VL53L0X(self.__i2c, config.address)

        distance = self.__readData()
        state = SensorState.ACTIVE if config.rangeMin < distance and config.rangeMax > distance else SensorState.IDLE

        self.__ultrasonicDistanceSensor = UltrasonicDistanceSensor(config.rangeMin, config.rangeMax, state)

    def __readData(self):
        value = self.__sensor.range
        return value
    
    def update(self):
        distance = self.__readData()
        print("[" + self.__sensorName + "] distance: {}".format(distance))
        self.__ultrasonicDistanceSensor.update(distance)

    def getSensor(self):
        return self.__ultrasonicDistanceSensor