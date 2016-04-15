from bt.base import Task, Decorator

class entreeTest(Task):

    def __init__(self, noeud, index=0):
        super().__init__()
        self.noeud = noeud
        self.indexEdge = index

    def run(self):
        entree = self.noeud.ina[self.indexEdge]
        if entree.w > 0:
            return Task.SUCCES
        return Task.ECHEC

class sortieTest(Task):
    def __init__(self, noeud, index=0):
        super().__init__()
        self.noeud = noeud
        self.indexEdge = index

    def run(self):
        sortie = self.noeud.oua[self.indexEdge]
        if sortie.w >= sortie.getCapacity():
            return Task.ECHEC
        return Task.SUCCES

#Traitement du minerai, au moins 50 tonnes
class machinePreTest(Task):
    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud
        self.noeud.isWorking = False

    def run(self):
        entree = self.noeud.ina[0]
        entree1 = self.noeud.ina[1]
        if entree.w >= 50 and entree1 >=50000:
            self.noeud.isWorking = True
        if entree.w < 1 or entree1 <1000:
            self.noeud.isWorking = False
        if self.noeud.isWorking:
            return Task.SUCCES
        return Task.ECHEC

