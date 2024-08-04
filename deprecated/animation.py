from dataclasses import dataclass
from enum import Enum, auto

class Color:
    def __init__(self, r: int, g: int, b: int, w: int):
        self.r = r
        self.g = g
        self.b = b
        self.w = w

    def getColor(self):
        return (self.r, self.g, self.b, self.w)

@dataclass
class AnimationFrame:
    newColor: Color
    rangeMin: float
    rangeMax: float

class AnimationState(Enum):
    RANGE = auto()
    IDLE = auto()
    TRANSITION = auto()

class Animation:
    def __init__(self, currentColor):
        self._currentColor = currentColor

    def compareColors(self, colorA: Color, colorB: Color):
        if(colorA.r != colorB.r):
            return False
        if(colorA.g != colorB.g):
            return False
        if(colorA.b != colorB.b):
            return False
        if(colorA.w != colorB.w):
            return False

        return True

    def nextFrame(self, frame: AnimationFrame):
        pass
        ### print("Frame")
        
    def isIdle(self):
        return False

    def getCurrentColor(self):
        return self._currentColor