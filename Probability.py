import random, math

class DistribTriang:

    def __init__(self, amin,amode, amax):
        self._min = amin
        self._mode = amode
        self._max = amax

    def mcInv(self):
        _U = random.random()
        _fc = (self._mode - self._min) / (self._max - self._min)
        if(_U < _fc):
            return math.floor(self._min + math.sqrt(_U * (self._max - self._min) * (self._mode - self._min)))
        else:
            return math.floor(self._max - math.sqrt( (1 -_U) * (self._max - self._min) * (self._max - self._mode)))

