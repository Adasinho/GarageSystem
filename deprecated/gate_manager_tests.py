import unittest

from gate_manager import GateManager, CarState
from ultrasonic_distance_sensor import UltrasonicDistanceSensor, SensorState as UltrasonicState
from digital_distance_sensor import DigitalDistanceSensor, SensorState as DigitalState
from magnetic_switch import MagneticSwitch

class TestCase(unittest.TestCase):
    def test_givenGateManagerWhenCarIsParkedThenStateIsParked(self):
        # given
        self.downUltrasonicSensor = UltrasonicDistanceSensor(0, 200, UltrasonicState.ACTIVE)
        self.upUltrasonicSensor = UltrasonicDistanceSensor(0, 150, UltrasonicState.IDLE)
        self.digitalSensor = DigitalDistanceSensor(DigitalState.ACTIVE)
        self.closeMagneticSwitch = MagneticSwitch(True)
        self.openMagneticSwitch = MagneticSwitch(False)
        self.gateManager = GateManager(self.downUltrasonicSensor, self.upUltrasonicSensor, self.digitalSensor, self.closeMagneticSwitch, self.openMagneticSwitch)

        # when
        self.downUltrasonicSensor.update(100)
        self.upUltrasonicSensor.update(100)
        self.digitalSensor.update(False)
        self.closeMagneticSwitch.update(True)
        self.openMagneticSwitch.update(False)
        self.gateManager.update()

        # then
        self.assertEqual(CarState.PARKED, self.gateManager.getCarState())

    def test_givenGateManagerWhenCarIsDepartingThenStateIsDeparting(self):
        # given
        self.downUltrasonicSensor = UltrasonicDistanceSensor(0, 200, UltrasonicState.IDLE)
        self.upUltrasonicSensor = UltrasonicDistanceSensor(0, 150, UltrasonicState.ACTIVE)
        self.digitalSensor = DigitalDistanceSensor(DigitalState.IDLE)
        self.closeMagneticSwitch = MagneticSwitch(False)
        self.openMagneticSwitch = MagneticSwitch(True)
        self.gateManager = GateManager(self.downUltrasonicSensor, self.upUltrasonicSensor, self.digitalSensor, self.closeMagneticSwitch, self.openMagneticSwitch)

        # when
        self.downUltrasonicSensor.update(100)
        self.upUltrasonicSensor.update(200)
        self.digitalSensor.update(True)
        self.closeMagneticSwitch.update(False)
        self.openMagneticSwitch.update(True)
        self.gateManager.update()

        # then
        self.assertEqual(CarState.DEPARTING, self.gateManager.getCarState())

    def test_givenGateManagerWhenCarIsEnteringThenStateIsEntering(self):
        # given
        self.downUltrasonicSensor = UltrasonicDistanceSensor(0, 200, UltrasonicState.IDLE)
        self.upUltrasonicSensor = UltrasonicDistanceSensor(0, 150, UltrasonicState.IDLE)
        self.digitalSensor = DigitalDistanceSensor(DigitalState.IDLE)
        self.closeMagneticSwitch = MagneticSwitch(False)
        self.openMagneticSwitch = MagneticSwitch(True)
        self.gateManager = GateManager(self.downUltrasonicSensor, self.upUltrasonicSensor, self.digitalSensor, self.closeMagneticSwitch, self.openMagneticSwitch)

        # when
        self.downUltrasonicSensor.update(100)
        self.upUltrasonicSensor.update(200)
        self.digitalSensor.update(True)
        self.closeMagneticSwitch.update(False)
        self.openMagneticSwitch.update(True)
        self.gateManager.update()

        # then
        self.assertEqual(CarState.ENTERING, self.gateManager.getCarState())

    def test_givenGateManagerWhenCarDroveOutOfTheGarageThenStateIsApartFrom(self):
        # given
        self.downUltrasonicSensor = UltrasonicDistanceSensor(0, 200, UltrasonicState.ACTIVE)
        self.upUltrasonicSensor = UltrasonicDistanceSensor(0, 150, UltrasonicState.IDLE)
        self.digitalSensor = DigitalDistanceSensor(DigitalState.ACTIVE)
        self.closeMagneticSwitch = MagneticSwitch(False)
        self.openMagneticSwitch = MagneticSwitch(True)
        self.gateManager = GateManager(self.downUltrasonicSensor, self.upUltrasonicSensor, self.digitalSensor, self.closeMagneticSwitch, self.openMagneticSwitch)

        # when
        self.downUltrasonicSensor.update(100)
        self.upUltrasonicSensor.update(200)
        self.digitalSensor.update(False)
        self.closeMagneticSwitch.update(False)
        self.openMagneticSwitch.update(True)
        self.gateManager.update()

        # then
        self.assertEqual(CarState.APART_FROM, self.gateManager.getCarState())

    def test_givenGateManagerWhenCarIsParkingThenStateIsParked(self):
        # given
        self.downUltrasonicSensor = UltrasonicDistanceSensor(0, 200, UltrasonicState.ACTIVE)
        self.upUltrasonicSensor = UltrasonicDistanceSensor(0, 150, UltrasonicState.IDLE)
        self.digitalSensor = DigitalDistanceSensor(DigitalState.ACTIVE)
        self.closeMagneticSwitch = MagneticSwitch(False)
        self.openMagneticSwitch = MagneticSwitch(True)
        self.gateManager = GateManager(self.downUltrasonicSensor, self.upUltrasonicSensor, self.digitalSensor, self.closeMagneticSwitch, self.openMagneticSwitch)

        # when
        self.downUltrasonicSensor.update(100)
        self.upUltrasonicSensor.update(100)
        self.digitalSensor.update(False)
        self.closeMagneticSwitch.update(False)
        self.openMagneticSwitch.update(True)
        self.gateManager.update()

        # then
        self.assertEqual(CarState.PARKED, self.gateManager.getCarState())

if __name__ == '__main__':
    unittest.main()