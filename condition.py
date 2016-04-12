from bt.base import Task, Decorator

class entreeTest(Task):

    def __init__(self, noeud, index=0):
        super().__init__()
        self.noeud = noeud
        self.indexEdge = index

    def run(self):
        entree = self.noeud.ina[self.indexEdge]
        if entree.w > 0:
            #print(self.noeud.name,': TRUE Il y a ', entree.w , entree.stockName)
            return Task.SUCCES
        #print(self.noeud.name,': FALSE Il y a ', entree.w , entree.stockName)
        return Task.ECHEC

class sortieTest(Task):
    def __init__(self, noeud, index=0):
        super().__init__()
        self.noeud = noeud
        self.indexEdge = index

    def run(self):
        sortie = self.noeud.oua[self.indexEdge]
        if sortie.w >= sortie.getCapacity():
            #print(self.noeud.name,': FALSE Il y a ', sortie.w, sortie.stockName)
            return Task.ECHEC

        #print(self.noeud.name,': TRUE Il y a ', sortie.w, sortie.stockName)
        return Task.SUCCES


