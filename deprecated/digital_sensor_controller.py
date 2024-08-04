from digital_distance_sensor import DigitalDistanceSensor, SensorState

import RPi.GPIO as GPIO

class DigitalSensorController:
    def __init__(self, dataPin, sensorName) -> None:
        self.__dataPin = dataPin
        self.__sensorName = sensorName
        self.__initialSettings()

        # define first state
        detected = self.__readData()
        if detected:
            state = SensorState.ACTIVE
        else:
            state = SensorState.IDLE
        
        self.__digitalDistanceSensor = DigitalDistanceSensor(state)

    def __initialSettings(self):
        # GPIO.setwarnings(False)
        # GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__dataPin, GPIO.IN)

    def __readData(self):
        data = GPIO.input(self.__dataPin)
        return not data

    def update(self):
        detected = self.__readData()
        ### print("[" + self.__sensorName + "] detected: ", detected)
        self.__digitalDistanceSensor.update(detected)

    def getSensor(self):
        return self.__digitalDistanceSensor