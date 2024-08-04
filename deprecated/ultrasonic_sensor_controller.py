from ultrasonic_distance_sensor import UltrasonicDistanceSensor, SensorState
from hcsr04sensor import sensor

class UltrasonicSensorController:
    def __init__(self, echoPin, trigPin, startOffset, endOffset, sensorName) -> None:
        self.__echoPin = echoPin
        self.__trigPin = trigPin
        self.__sensorName = sensorName

        distance = self.__readData() 
        state = SensorState.ACTIVE if startOffset < distance and endOffset > distance else SensorState.IDLE

        self.__ultrasonicDistanceSensor = UltrasonicDistanceSensor(startOffset, endOffset, state)

    def __readData(self):
        value = sensor.Measurement(self.__trigPin, self.__echoPin)
        raw_distance = value.raw_distance(sample_wait=0.05)
        distance = round(raw_distance, 1)
        return distance

    def update(self):
        distance = self.__readData()
        ### print("[" + self.__sensorName + "] distance: ", distance)
        self.__ultrasonicDistanceSensor.update(distance)

    def getSensor(self):
        return self.__ultrasonicDistanceSensor