import time

class Timer:
    def __init__(self, timeout) -> None:
        self.__startTime = time.time()
        self.__timeout = timeout
        
    def isEnd(self):
        now = time.time()
        print("startTime:", self.__startTime, ", now:", now)
        print("passed time:", (self.__startTime + self.__timeout) < now)
        return (self.__startTime + self.__timeout) < now