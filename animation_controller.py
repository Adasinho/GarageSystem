import neopixel
from animation_manager import AnimationManager

class AnimationController:
    def __init__(self, dataPin, numberOfPixels, brightness) -> None:
        self.__dataPin = dataPin
        self.__numberOfPixels = numberOfPixels
        self.__defaultBrightness = brightness
        self.__strip = neopixel.NeoPixel(dataPin, numberOfPixels, brightness=brightness, auto_write=False, pixel_order=neopixel.RGBW)

        self.__animationManager = AnimationManager(self.__strip)

    def update(self):
        self.__animationManager.update()

    def getManager(self):
        return self.__animationManager