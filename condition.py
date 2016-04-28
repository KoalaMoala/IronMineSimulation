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

#Traitement du minerai, au moins 50 tonnes et 50000L de produits
class machinePreTest(Task):
    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud
        self.noeud.isWorking = False

    def run(self):
        entree = self.noeud.ina[1]
        entree1 = self.noeud.ina[0]
        if entree.w >= 50 and entree1.w >=50000:
            self.noeud.isWorking = True
        if entree.w < 10 or entree1.w <10000:
            self.noeud.isWorking = False
        if self.noeud.isWorking:
            return Task.SUCCES
        return Task.ECHEC

#Approvisionnement train au besoin
class trainTest(Task):
    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud
        self.noeud.train = False

    def run(self):
        chemical = self.noeud.oua[0].w
        chemicalMix = self.noeud.oua[0].nodeTo.oua[0].w
        if(chemical+chemicalMix+self.noeud.loadQty <50000):
            self.noeud._num += 1
            self.noeud.loadQty = 300000
        return Task.SUCCES

class trainLoadTest(Task):
    def __init__(self,noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        if(self.noeud.loadQty >= 30000):
            return Task.SUCCES
        return Task.ECHEC

class trainExitTest(Task):
    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        sortie = self.noeud.oua[0]
        if sortie.w > sortie.getCapacity() - 30000:
            return Task.ECHEC
        return Task.SUCCES


class mineTest(Task):
    def __init__(self,noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        if(self.noeud.dailyQty >=1):
            return Task.SUCCES
        return Task.ECHEC

class mineExitTest(Task):
    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        sortie = self.noeud.oua[0]
        if sortie.w >= sortie.getCapacity() - self.noeud._num+1:
            return Task.ECHEC
        return Task.SUCCES

class mixerTest(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        entree = self.noeud.ina[0]
        if entree.w >= 10000:
            return Task.SUCCES
        return Task.ECHEC

class mixerExitTest(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        sortie = self.noeud.oua[0]
        if sortie.w >= sortie.getCapacity()-9000:
            return Task.ECHEC
        return Task.SUCCES

class oreProcTest(Task):
    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        sortie = self.noeud.oua[0]
        if sortie.w >= sortie.getCapacity()-10:
            return Task.ECHEC
        return Task.SUCCES


#Evacuation ship au besoin
class shipTest(Task):
    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud
        self.noeud.ship = False

    def run(self):
        if(self.noeud.ina[0].w >=2000):
            self.noeud.ship = True
            return Task.SUCCES
        return Task.ECHEC