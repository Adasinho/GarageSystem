from time_to_flight_sensor_controller import TimeToFlightSensorController

import time
import RPi.GPIO as GPIO

if __name__ == '__main__':
    print("start")

    GPIO.setwarnings(False)
    # GPIO.setmode(GPIO.BOARD)

    ECHO1_PIN = 27
    TRIG1_PIN = 17
    TRIG2_PIN = 3
    ECHO2_PIN = 4
    START_OFFSET = 0
    END_OFFSET = 800

    print("2.")
    sensor2 = TimeToFlightSensorController(START_OFFSET, END_OFFSET, "Czujnik ultradźwiękowy (góra)", 0x29)
    time.sleep(0.1)

    try:
        while True:
            sensor2.update()            
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("end")