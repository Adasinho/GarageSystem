from animation_player import AnimationPlayer
from animation import AnimationFrame, Color, AnimationState

class AnimationManager:
    def __init__(self, strip) -> None:
        self.__state = AnimationState.IDLE
        self.__animationPlayer = AnimationPlayer(strip, self.__state)
        self.__animationFrame = AnimationFrame(Color(255,255,255,255), 0, 0, 100)

    def update(self):
        self.__animationPlayer.update(self.__animationFrame)
        print("Animation state: ", self.__state)

    def updateFrame(self, frame: AnimationFrame):
        self.__animationFrame = frame
        
    def changeAnimation(self, newAnimation: AnimationState):
        if self.__state == newAnimation:
            return

        if newAnimation == AnimationState.IDLE:
            self.__state = AnimationState.TRANSITION
        elif newAnimation == AnimationState.RANGE:
            self.__state = AnimationState.RANGE
        
        self.__animationPlayer.changeAnimation(self.__state, self.__animationFrame)