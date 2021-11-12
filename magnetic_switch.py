class MagneticSwitch:
    def __init__(self, active) -> None:
        self.__active = active

    def update(self, active):
        self.__active = active

    def isActive(self):
        return self.__active