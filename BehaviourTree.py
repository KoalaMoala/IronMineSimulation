from bt.base import *
from condition import *
from action import *
from bt.decorator import *

def createBehaviorTree(noeud):
    x = machineTache(noeud)
    condition1 = entreeTest(noeud)

    deco = Delay(noeud.tcycle)
    deco.add_child(x)

    racine = SequenceStar()
    root= Repeater()
    root.add_child(racine)

    selector1 = Sequence()
    selector1.add_child(condition1)
    racine.add_child(selector1)
    racine.add_child(deco)


