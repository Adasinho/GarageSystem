from digital_sensor_controller import DigitalSensorController
from gate_controller import GateController
from magnectic_switch_controller import MagneticSwitchController
from animation_controller import AnimationController
from time_to_flight_sensor_controller import TimeToFlightSensorController, TimeToFlightSensorParams
from utils import parseCarState, setSensorsUniqueAddress

import time
import RPi.GPIO as GPIO
import board
import os

if __name__ == '__main__':
    print("start")

    GPIO.setwarnings(False)

    ECHO1_PIN = 27
    TRIG1_PIN = 17
    TRIG2_PIN = 3
    ECHO2_PIN = 4
    RANGE_MIN = 0
    RANGE_MAX = 400

    DIGITAL_DATA_PIN = 23

    SWITCH1_PIN = 24
    SWITCH2_PIN = 22

    STRIP_PIN = board.D18
    
    sensor1Config = TimeToFlightSensorParams(RANGE_MIN, RANGE_MAX, "Czujnik ultradźwiękowy (dół)", 0x29, board.D26)
    sensor2Config = TimeToFlightSensorParams(RANGE_MIN, RANGE_MAX, "Czujnik ultradźwiękowy (góra)", 0x30, board.D19)
    setSensorsUniqueAddress([sensor1Config, sensor2Config])

    sensor1 = TimeToFlightSensorController(sensor1Config)
    sensor2 = TimeToFlightSensorController(sensor2Config)
    digitalSensor = DigitalSensorController(DIGITAL_DATA_PIN, "Czujnik LIDAR")
    magneticSwitch1 = MagneticSwitchController(SWITCH1_PIN)
    magneticSwitch2 = MagneticSwitchController(SWITCH2_PIN)
    animationController = AnimationController(STRIP_PIN, 30, 255)

    gateController = GateController(sensor1, sensor2, digitalSensor, magneticSwitch1, magneticSwitch2, animationController)

    try:
        while True:
            os.system("clear")
            print("loop")

            gateController.update()
            carState = gateController.getCarState()
            parseCarState(carState)
            
            time.sleep(1)

    except KeyboardInterrupt:
        print("end")