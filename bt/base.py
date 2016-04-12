from abc import ABCMeta, abstractmethod

class Task(object, metaclass=ABCMeta):
    """ Classe base pour un noeud du Behavior Tree """
    ECHEC, SUCCES, RUNNING = range(3)  # compatibilite: False est un ECHEC et True est un SUCCES

    def __init__(self):
        self._children = []
        self.index = 0

    @abstractmethod
    def run(self):
        return

    def add_child(self, c):
        self._children.append(c)

class Decorator(Task):
    """ Decorator """
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()

    def add_child(self, c):
        if len(self._children) < 1:
            super(Decorator, self).add_child(c)


class Selector(Task):
    """ Selector """

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(self.index, len(self._children)):
            status = self._children[i].run()
            if status == Task.SUCCES:
                return Task.SUCCES
            elif status == Task.RUNNING:
                return Task.RUNNING
        return Task.ECHEC

    def add_child(self, c):
        super(Selector, self).add_child(c)


class SelectorStar(Task):
    """ Selector star """

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(self.index, len(self._children)):
            status = self._children[i].run()
            if status == Task.SUCCES:
                self.index = 0
                return Task.SUCCES
            elif status == Task.RUNNING:
                self.index = i
                return Task.RUNNING
        self.index = 0
        return Task.ECHEC

    def add_child(self, c):
        super(SelectorStar, self).add_child(c)


class Sequence(Task):
    """ Sequence """

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(self.index, len(self._children)):
            status = self._children[i].run()
            if status == Task.ECHEC:
                return Task.ECHEC
            elif status == Task.RUNNING:
                return Task.RUNNING
        return Task.SUCCES

    def add_child(self, c):
        super().add_child(c)


class SequenceStar(Task):
    """ Sequence star """

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(self.index, len(self._children)):
            status = self._children[i].run()
            if status == Task.ECHEC:
                self.index = 0
                return Task.ECHEC
            elif status == Task.RUNNING:
                self.index = i
                return Task.RUNNING
        self.index = 0
        return Task.SUCCES

    def add_child(self, c):
        super().add_child(c)
