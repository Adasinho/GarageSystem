from typing import List
from gate_manager import CarState
from time_to_flight_sensor_controller import TimeToFlightSensorParams

import board
from digitalio import DigitalInOut
from adafruit_vl53l0x import VL53L0X
import VL53L1X

def parseCarState(carState: CarState):
    if carState == CarState.ENTERING:
        print("ENTERING")
    elif carState == CarState.APART_FROM:
        print("APART_FROM")
    elif carState == CarState.DEPARTING:
        print("DEPARTING")
    elif carState == CarState.PARKED:
        print("PARKED")
    else:
        print("UNDEFINED")
        
def setSensorsUniqueAddress(configs: List[TimeToFlightSensorParams]):
    # declare the singleton variable for the default I2C bus
    i2c = board.I2C()

    # declare the digital output pins connected to the "SHDN" pin on each VL53L0X sensor
    xshut = []
    for config in configs:
        xshut.append(DigitalInOut(config.xshutPin))
    
    for power_pin in xshut:
        # make sure these pins are a digital output, not a digital input
        power_pin.switch_to_output(value=False)
        # These pins are active when Low, meaning:
        #   if the output signal is LOW, then the VL53L0X sensor is off.
        #   if the output signal is HIGH, then the VL53L0X sensor is on.
    # all VL53L0X sensors are now off

    # initialize a list to be used for the array of VL53L0X sensors
    vl53 = []

    # now change the addresses of the VL53L0X sensors
    for i, power_pin in enumerate(xshut):
        # turn on the VL53L0X to allow hardware check
        power_pin.value = True
        # instantiate the VL53L0X sensor on the I2C bus & insert it into the "vl53" list
        vl53.insert(i, VL53L1X.VL53L1X(i2c_bus=1))  # also performs VL53L0X hardware check
        # no need to change the address of the last VL53L0X sensor
        if i < len(xshut) - 1:
            #vl53.insert(i, VL53L1X(i2c, i + 0x30))  # also performs VL53L0X hardware check
            # default address is 0x29. Change that to something else
            vl53[i].open()
            vl53[i].change_address(new_address=(i + 0x30))  # address assigned should NOT be already in use
