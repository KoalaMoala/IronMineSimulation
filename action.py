from bt.base import Task

class machineTache(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        for ina in self.noeud.ina:
            ina.w -= 1
        return Task.SUCCES

class machinePostTache(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        for oua in self.noeud.oua:
            oua.w += 1
        return Task.SUCCES


class machineShip(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        for ina in self.noeud.ina:
            ina.w -= 2000
        return Task.SUCCES

class machineTrain(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud
        self.index = 0

    def run(self):
        if(self.index < 10):
            self.index+=1
            self.noeud.oua[0].w += 30000
            return Task.RUNNING
        else:
            self.index = 0
            return Task.SUCCES

class machineMine(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud
        self.index = 24

    def run(self):
        if(self.index < self.noeud.dailyQty):
            self.index-=1
            self.noeud.dailyQty -= 2
            self.noeud._num = 2
            return Task.SUCCES
        else:
            self.index = 24
            self.noeud.dailyQty -= 1
            self.noeud._num = 1
            return Task.SUCCES

class machinePostMine(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        self.noeud.oua[0].w += self.noeud._num
        return Task.SUCCES

class machinePostMixer(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        self.noeud.oua[0].w += 10000
        return Task.SUCCES

class machineMixer(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        self.noeud.ina[0].w -= 10000
        return Task.SUCCES

class machineOreProcess(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        self.noeud.ina[1].w -= 1
        self.noeud.ina[0].w -= 1000
        return Task.SUCCES

class machineShip(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud
        self.index = 0
        self.noeud._num = 0

    def run(self):
        if(self.index < 10):
            self.index+=1
            self.noeud.ina[0] -= 200
            return Task.RUNNING
        else:
            self.index = 0
            self.noeud._num += 1
            return Task.SUCCES
