from Workshop import Workshop
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
        self.workshops.append(Workshop("Unloading Dock", self.behaviourTrees[0], None, None))
        self.workshops.append(Workshop("Mixer", self.behaviourTrees[0], None, None))
        self.workshops.append(Workshop("Mine", self.behaviourTrees[0], None, None))
        self.workshops.append(Workshop("Ore Processing", self.behaviourTrees[0], None, None))
        self.workshops.append(Workshop("Loading Dock", self.behaviourTrees[0], None, None))
