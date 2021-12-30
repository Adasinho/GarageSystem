import neopixel
from animation import Animation, AnimationFrame, Color, AnimationState
from timer import Timer

WHITE_COLOR = Color(255, 255, 255, 0)
RED_COLOR = Color(255, 0, 0, 0)
GREEN_COLOR = Color(0, 255, 0, 0)
ORANGE_COLOR = Color(255, 165, 0, 0)

class AnimationTransition(Animation):
    def __init__(self, currentColor: Color, targetColor: Color, strip: neopixel.NeoPixel):
        super().__init__(currentColor)
        self.__targetColor = targetColor
        self.__strip = strip

    def nextFrame(self, frame: AnimationFrame):
        if(not self.compareColors(self._currentColor, self.__targetColor)):
            newColor: Color = self.transitionStep(self._currentColor, self.__targetColor, 20)
            self._currentColor = newColor
            self.__strip.fill(newColor.getColor())
            self.__strip.show()

    def transitionStep(self, fromColor: Color, targetColor: Color, step) -> Color:
        newColor = Color(0, 0, 0, 0)
        if(fromColor.r != targetColor.r):
            newColor.r = fromColor.r + step if fromColor.r < targetColor.r else fromColor.r - step
            newColor.r = targetColor.r if newColor.r > targetColor.r else newColor.r
        else:
            newColor.r = targetColor.r
        if(fromColor.g != targetColor.g):
            newColor.g = fromColor.g + step if fromColor.g < targetColor.g else fromColor.g - step
            newColor.g = targetColor.g if newColor.g > targetColor.g else newColor.g
        else:
            newColor.g = targetColor.g
        if(fromColor.b != targetColor.b):
            newColor.b = fromColor.b + step if fromColor.b < targetColor.b else fromColor.b - step
            newColor.b = targetColor.b if newColor.b > targetColor.b else newColor.b
        else:
            newColor.b = targetColor.b
        if(fromColor.w != targetColor.w):
            newColor.w = fromColor.w + step if fromColor.w < targetColor.w else fromColor.w - step
            newColor.w = targetColor.w if newColor.w > targetColor.w else newColor.w
        else:
            newColor.w = targetColor.w

        ### print("[fromColor] red: ", fromColor.r, " green: ", fromColor.g, " blue: ", fromColor.b)
        ### print("[targetColor] red: ", targetColor.r, " green: ", targetColor.g, " blue: ", targetColor.b)
        ### print("[newColor] red: ", newColor.r, " green: ", newColor.g, " blue: ", newColor.b)

        return newColor

class AnimationStableColor(Animation):
    def __init__(self, currentColor: Color, targetColor: Color, strip: neopixel.NeoPixel):
        super().__init__(currentColor)
        self.__targetColor = targetColor
        self.__strip = strip
        self.__strip.fill(targetColor.getColor())
        self.__strip.show()

class AnimationRange(Animation):
    def __init__(self, currentColor: Color, rangeMin, rangeMax, strip: neopixel.NeoPixel):
        super().__init__(currentColor)
        self.__strip = strip
        self.__rangeMin = rangeMin
        self.__rangeMax = rangeMax
        self.__steps = 7
        self.__stepsArray = self.__initStepsArray()
        self.__timer = Timer(10)
        self.__lastStep = 100
        ### print("Start timer")
    
    def nextFrame(self, frame: AnimationFrame):
        step = self.__valueToStep(frame.value)
        if step != self.__lastStep:
            self.__lastStep = step
            self.__timer = Timer(10)
            ### print("Start timer")
            newColor: Color = self.__stepsArray[step]
            ### print("step:", step, "r:", newColor.r, "g:", newColor.g, "b:", newColor.b)
            self._currentColor = newColor
            self.__strip.fill(newColor.getColor())
            self.__strip.show()
            
    def restartAnimation(self):
        self.__timer = Timer(10)
            
    def isIdle(self):
        return self.__timer.isEnd()

    def __initStepsArray(self):
        stepsArray = []

        stepsArray.append(RED_COLOR)
        stepsArray.append(Color(255, 50, 0, 0))
        stepsArray.append(Color(255, 100, 0, 0))
        stepsArray.append(ORANGE_COLOR)
        stepsArray.append(Color(200, 165, 0, 0))
        stepsArray.append(Color(100, 200, 0, 0))
        stepsArray.append(GREEN_COLOR)

        return stepsArray

    def __valueToStep(self, value) -> int:
        offset = self.__rangeMin
        maximum = self.__rangeMax - offset
        ### print("maximum", maximum)

        offsetValue = value - offset
        ### print("offsetValue", offsetValue)
        stepValue = maximum / (self.__steps - 1)
        ### print("stepValue", stepValue)
        ret = (offsetValue / stepValue)
        ### print("ret [1]", ret)
        ret = round(ret) - 1
        ### print("ret [2]", ret)

        if ret < 0:
            ret = 0
        elif ret > (self.__steps - 1):
            ret = self.__steps - 1

        ### print("value:", value, "ret:", ret)
        return ret

class AnimationPlayer:
    def __init__(self, strip: neopixel.NeoPixel, currentState: AnimationState):
        self.__currentColor = WHITE_COLOR
        self.__strip = strip
        self.__state = currentState
        self.__animation = AnimationStableColor(self.__currentColor, WHITE_COLOR, self.__strip)

        self.__strip.fill(WHITE_COLOR.getColor())
        self.__strip.show()
        ### print("AnimationPlayer init")

    def changeAnimation(self, newState: AnimationState, frame: AnimationFrame):
        if self.__state != newState:
            if newState == AnimationState.IDLE:
                self.__state = newState
                self.__animation = AnimationStableColor(self.__currentColor, frame.newColor, self.__strip)
            elif newState == AnimationState.RANGE:
                self.__state = newState
                self.__animation = AnimationRange(self.__currentColor, frame.rangeMin, frame.rangeMax, self.__strip)
            elif newState == AnimationState.TRANSITION:
                self.__state = newState
                self.__animation = AnimationTransition(self.__currentColor, frame.newColor, self.__strip)
    
    def isIdle(self):
        return self.__animation.isIdle()
    
    def restartAnimation(self):
        self.__animation.restartAnimation()

    def update(self, frame: AnimationFrame):
        self.__currentColor = self.__animation.getCurrentColor()
        self.__animation.nextFrame(frame)