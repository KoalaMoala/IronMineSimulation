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


