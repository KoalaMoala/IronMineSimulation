from workshop import Workshop
from transit import Transit
from BehaviourTree import BehaviorTree
import config


class System:
    def __init__(self):
        self.workshops = []
        self.transits = []

    def init_workshop(self):
        self.workshops.append(Workshop("Unloading Dock", config._ud[0],  config._ud[1]))
        self.workshops.append(Workshop("Mixer", config._mx[0],  config._mx[1]))
        self.workshops.append(Workshop("Mine", config._mi[0],  config._mi[1]))
        self.workshops.append(Workshop("Ore Processing", config._op[0],  config._op[1]))
        self.workshops.append(Workshop("Loading Dock", config._ld[0],  config._ld[1]))

    def init_transit(self):
        # instancing transits with config data
        self.transits.append(Transit("Tank", self.workshops[1], self.workshops[3], config._eta[0], config._eta[1], config._eta[2], config._eta[3]))
        self.workshops[1].addOutEdge(self.transits[0])
        self.workshops[3].addInEdge(self.transits[0])

        self.transits.append(Transit("Pit 1", self.workshops[2], self.workshops[3],config._ep1[0], config._ep1[1], config._ep1[2], config._ep1[3]))
        self.workshops[2].addOutEdge(self.transits[1])
        self.workshops[3].addInEdge(self.transits[1])

        self.transits.append(Transit("Pit 2", self.workshops[3], self.workshops[4], config._ep2[0], config._ep2[1], config._ep2[2], config._ep2[3]))
        self.workshops[3].addOutEdge(self.transits[2])
        self.workshops[4].addInEdge(self.transits[2])

        self.transits.append(Transit("Transit", self.workshops[0], self.workshops[1], config._etr[0], config._etr[1], config._etr[2], config._etr[3]))
        self.workshops[0].addOutEdge(self.transits[3])
        self.workshops[1].addInEdge(self.transits[3])

    def init_behavior(self):
        for ws in self.workshops:
            ws.setBehavior(BehaviorTree(ws))

    def render(self,g, w, h):
        for ed in self.transits:
            ed.render(g,w,h)
        for ws in self.workshops:
            ws.render(g,w,h)

    def update(self):
        for ws in self.workshops:
            ws.update()

    def computeDailyQty(self):
        for ws in self.workshops:
            if(ws.name == "Mine"):
                ws.computeDailyQty()
                return

    def getTrainShip(self):
        res = []
        for ws in self.workshops:
            if(ws.name == "Unloading Dock" or ws.name== "Loading Dock"):
                res.append(ws._num)
        return res



