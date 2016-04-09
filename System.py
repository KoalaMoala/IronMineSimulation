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
        self.workshops.append(Workshop("unloadingDock", self.behaviourTrees[0], ["base", "solvant"], None,
                                       [100000, 100000], ["base", "solvant"], None, [100000, 100000]))
        self.workshops.append(Workshop("mixer", self.behaviourTrees[0], ["base", "solvant"], None,
                                       [100000, 100000], ["melange"], None, [100000]))
