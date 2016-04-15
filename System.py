from workshop import Workshop
from transit import Transit
from BehaviourTree import BehaviorTree


class System:
    def __init__(self):
        self.workshops = []
        self.transits = []

    def init_workshop(self):
        self.workshops.append(Workshop("Unloading Dock", {"x": 100, "y": 100}, 1))
        self.workshops.append(Workshop("Mixer", {"x": 350, "y": 150},2))
        self.workshops.append(Workshop("Mine", {"x": 100, "y": 400},1))
        self.workshops.append(Workshop("Ore Processing", {"x": 350, "y": 350},2))
        self.workshops.append(Workshop("Loading Dock", {"x": 600, "y": 350},1))

    def init_transit(self):
        # Assumed that container capacity is 10.000L. No indication anywhere.
        self.transits.append(Transit("Tank", self.workshops[1], self.workshops[3], "Chemical mix", 100000, 0, 'L'))
        self.workshops[1].addOutEdge(self.transits[0])
        self.workshops[3].addInEdge(self.transits[0])

        # Assumed that pit 1 capacity is 200t. No indication anywhere.
        self.transits.append(Transit("Pit 1", self.workshops[2], self.workshops[3], "Ore", 200, 45, 'T'))
        self.workshops[2].addOutEdge(self.transits[1])
        self.workshops[3].addInEdge(self.transits[1])

        # Assumed that pit 2 capacity is 200t. No indication anywhere.
        self.transits.append(Transit("Pit 2", self.workshops[3], self.workshops[4], "Iron", 2200, 0, 'T'))
        self.workshops[3].addOutEdge(self.transits[2])
        self.workshops[4].addInEdge(self.transits[2])

        self.transits.append(Transit("Transit", self.workshops[0], self.workshops[1], "Chemical", 300000,10000, 'L'))
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
                print("aaaa")
                ws.computeDailyQty()
                return



