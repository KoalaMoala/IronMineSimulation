import random, math

class DistribTriang:

    def __init__(self, amin,amode, amax):
        self._min = amin
        self._mode = amode
        self._max = amax

    def fct(self,x):
        if(x >= self._min and x <= self._mode):
            return 2 * (x-self._min) / ((self._max - self._min)*(self._mode - self._min))
        elif(x>self._mode and x<self._max):
            return 2 * (self._max-x) / ((self._max - self._min)*(self._max - self._mode))
        else:
            return 0

    def mcInv(self):
        for i in range(100):
            x=random.random()*20+10
            y=random.random()*2/(self._max - self._min)
            if y<self.fct(x):
                return math.floor(x)
        return self._min
