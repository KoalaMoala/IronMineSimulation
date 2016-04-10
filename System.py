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
        self.workshops.append(Workshop("unloadingDock", self.behaviourTrees[0], None, None))
        self.workshops.append(Workshop("mixer", self.behaviourTrees[0], None, None))
