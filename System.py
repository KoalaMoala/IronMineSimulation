from workshop import Workshop
from transit import Transit
from BehaviourTree import BehaviorTree


class System:
    def __init__(self):
        self.workshops = []
        self.transits = []

    def init_workshop(self):
        self.workshops.append(Workshop("Unloading Dock", {"x": 50, "y": 50}))
        self.workshops.append(Workshop("Mixer", {"x": 250, "y": 100}))
        self.workshops.append(Workshop("Mine", {"x": 50, "y": 350}))
        self.workshops.append(Workshop("Ore Processing", {"x": 250, "y": 350}))
        self.workshops.append(Workshop("Loading Dock", {"x": 450, "y": 350}))

    def init_transit(self):
        # Assumed that container capacity is 10.000L. No indication anywhere.
        self.transits.append(Transit("Tank", self.workshops[1], self.workshops[3], "Chemical mix", 10000))
        self.workshops[1].addOutEdge(self.transits[0])
        self.workshops[3].addInEdge(self.transits[0])

        # Assumed that pit 1 capacity is 200t. No indication anywhere.
        self.transits.append(Transit("Pit 1", self.workshops[2], self.workshops[3], "Ore", 200))
        self.workshops[2].addOutEdge(self.transits[1])
        self.workshops[3].addInEdge(self.transits[1])

        # Assumed that pit 2 capacity is 200t. No indication anywhere.
        self.transits.append(Transit("Pit 2", self.workshops[3], self.workshops[4], "Iron", 200))
        self.workshops[3].addOutEdge(self.transits[2])
        self.workshops[4].addInEdge(self.transits[2])



    def init_behavior(self):
        for ws in self.workshops:
            ws.setBehavior(BehaviorTree(ws))

    def render(self,g, w, h):
        for ws in self.workshops:
            ws.render(g,w,h)
        for ed in self.transits:
            ed.render(g,w,h)

    def update(self):
        for ws in self.workshops:
            ws.update()



