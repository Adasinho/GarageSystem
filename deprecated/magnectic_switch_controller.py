from magnetic_switch import MagneticSwitch

import RPi.GPIO as GPIO

class MagneticSwitchController:
    def __init__(self, dataPin) -> None:
        ### print("MAGNETIC")
        self.__dataPin = dataPin
        self.__initialSettings()

        active = self.__readData()
        self.__magneticSwitch = MagneticSwitch(active)

    def __initialSettings(self):
        # GPIO.setwarnings(False)
        # GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__dataPin, GPIO.IN)

    def __readData(self):
        data = GPIO.input(self.__dataPin)
        return not data

    def update(self):
        active = self.__readData()
        self.__magneticSwitch.update(active)

    def getSensor(self):
        return self.__magneticSwitch