from bt.base import Sequence, SequenceStar
from condition import *
from action import *
from bt.decorator import *

class BehaviorTree():

    def __init__(self, noeud):
        if(noeud.name == "Mine"):
            self.createBTMine(noeud)
        elif(noeud.name == "Unloading Dock"):
            self.createBTUnloadingDock(noeud)
        elif(noeud.name == "Ore Processing"):
            self.createBTOreProcessing(noeud)
        elif(noeud.name == "Mixer"):
            self.createBTMixer(noeud)
        elif(noeud.name == "Loading Dock"):
            self.createBTLoadingDock(noeud)

    def createBTUnloadingDock(self, noeud):
        self.root = SequenceStar()


        dela = Delay(noeud.tcycle)
        dela.add_child(machineTrain(noeud))

        sequence = Sequence()
        sequence.add_child(trainLoadTest(noeud))

        rep = Repeater()
        seq2 = Sequence()
        seq2.add_child(trainExitTest(noeud))
        seq2.add_child(machinePostTrain(noeud))
        rep.add_child(seq2)

        self.root.add_child(trainTest(noeud))
        self.root.add_child(sequence)
        self.root.add_child(dela)
        self.root.add_child(rep)


    def createBTOreProcessing(self, noeud):
        self.root = SequenceStar()

        x = machineOreProcess(noeud)
        deco = Delay(noeud.tcycle)
        deco.add_child(x)

        subroot = SequenceStar()

        repeater = Repeater()
        selector2 = Sequence()
        selector2.add_child(oreProcTest(noeud))
        selector2.add_child(machinePostOreProc(noeud))
        repeater.add_child(selector2)

        subroot.add_child(deco)
        subroot.add_child(repeater)

        self.root.add_child(machinePreTest(noeud))
        self.root.add_child(subroot)

    def createBTMine(self,noeud):
        self.root = SequenceStar()
        self.root.add_child(mineTest(noeud))

        dela = Delay(noeud.tcycle)
        dela.add_child(machineMine(noeud))

        repeater = Repeater()
        selector = Sequence()

        selector.add_child(mineExitTest(noeud))
        selector.add_child(machinePostMine(noeud))

        repeater.add_child(selector)

        self.root.add_child(dela)
        self.root.add_child(repeater)


    def createBTMixer(self,noeud):
        self.root = SequenceStar()

        dela = Delay(noeud.tcycle)
        dela.add_child(machineMixer(noeud))

        repeater = Repeater()
        selector = Sequence()

        selector.add_child(mixerExitTest(noeud))
        selector.add_child(machinePostMixer(noeud))

        repeater.add_child(selector)

        self.root.add_child(mixerTest(noeud))
        self.root.add_child(dela)
        self.root.add_child(repeater)


    def createBTLoadingDock(self, noeud):
        self.root = SequenceStar()

        rep = Repeater()
        rep.add_child(machineShip(noeud))

        dela = Delay(noeud.tcycle)
        dela.add_child(rep)

        self.root.add_child(shipTest(noeud))
        self.root.add_child(dela)




    def update(self):
        self.root.run()
