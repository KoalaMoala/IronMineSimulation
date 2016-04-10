from Workshop import Workshop
from Transit import Transit
from BehaviourTree import BehaviourTree


class System:
    def __init__(self):
        self.workshops = []
        self.behaviourTrees = []
        self.transits = []
        self.input = []
        self.output = []

    def init_behaviour_trees(self):
        self.behaviourTrees.append(BehaviourTree())

    def init_workshop(self):
        self.workshops.append(Workshop("Unloading Dock", self.behaviourTrees[0]))
        self.workshops.append(Workshop("Mixer", self.behaviourTrees[0]))
        self.workshops.append(Workshop("Mine", self.behaviourTrees[0]))
        self.workshops.append(Workshop("Ore Processing", self.behaviourTrees[0]))
        self.workshops.append(Workshop("Loading Dock", self.behaviourTrees[0]))

    def init_transit(self):
        # Assumed that container capacity is 10.000L. No indication anywhere.
        self.transits.append(Transit("Tank", self.workshops[1], self.workshops[3], ["Chemical mix"], [10000]))

        # Assumed that pit 1 capacity is 200t. No indication anywhere.
        self.transits.append(Transit("Pit 1", self.workshops[2], self.workshops[3], ["Ore"], [200]))

        # Assumed that pit 2 capacity is 200t. No indication anywhere.
        self.transits.append(Transit("Pit 2", self.workshops[3], self.workshops[4], ["Iron"], [200]))

        # Adding connections to workshops objects
        self.workshops[1].set_transit(None, [self.transits[0]])  # Mixer
        self.workshops[2].set_transit(None, [self.transits[1]])  # Mine
        self.workshops[3].set_transit([self.transits[0], self.transits[1]], self.transits[2])  # Ore Processing
        self.workshops[4].set_transit([self.transits[2]], None)  # Loading Dock

