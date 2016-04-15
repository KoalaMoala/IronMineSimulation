from bt.base import Task

class machinePreTache(Task):

    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        print("action: machinePreTache")
        return Task.SUCCES

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

class machineOreProc(Task):
    def __init__(self, noeud):
        super().__init__()
        self.noeud = noeud

    def run(self):
        for ina in self.noeud.ina:
            ina.w -= 2000
        return Task.SUCCES
