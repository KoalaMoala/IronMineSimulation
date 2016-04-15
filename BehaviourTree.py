from bt.base import Sequence, SequenceStar
from condition import *
from action import machineTache, machinePostTache
from bt.decorator import *

class BehaviorTree():

    def __init__(self, noeud):
        self.createBehaviorTree(noeud)

    def createBehaviorTree(self, noeud):
        x = machineTache(noeud)
        deco = Delay(noeud.tcycle)
        deco.add_child(x)

        self.root = SequenceStar()

        selector1 = Sequence()
        for i in range(len(noeud.ina)):
            selector1.add_child(entreeTest(noeud,i))

        repeater = Repeater()
        selector2 = Sequence()
        for i in range(len(noeud.oua)):
            selector2.add_child(sortieTest(noeud,i))
        selector2.add_child(machinePostTache(noeud))
        repeater.add_child(selector2)

        self.root.add_child(selector1)
        self.root.add_child(deco)
        self.root.add_child(repeater)

    def createBTUnloadingDock(self):
        self.root = SequenceStar()

    def createBTOreProcessing(self, noeud):
        self.root = SequenceStar()

        x = machineTache(noeud)
        deco = Delay(noeud.tcycle)
        deco.add_child(x)

        subroot = SequenceStar()

        repeater = Repeater()
        selector2 = Sequence()
        for i in range(len(noeud.oua)):
            selector2.add_child(sortieTest(noeud,i))
        selector2.add_child(machinePostTache(noeud))
        repeater.add_child(selector2)

        subroot.add_child(deco)
        subroot.add_child(repeater)

        self.root.add_child(machinePreTest(noeud))
        self.root.add_child(subroot)

    def update(self):
        self.root.run()
