""" Renderin d'un modele avec Tkinter. """
from System import System
from tkinter import *
from time import sleep
import config
import time

doRenderTk = True  # choix de faire un rendering Tk ou pas


class Modele(object):
    """ Modele pour simulation. """

    def __init__(self, system, master=None):
        self.system = system
        self.init_modele()  # init du modele lui-meme
        # canvas pour le rendering graphique
        self.canvas_size = (800, 600)  # taille du canvas pour le rendering
        if master is not None:  # fenetre de rendering si necessaire
            self.refreshTk = config._speed
            self.start = time.time()
            self.waitTk = 3
            self.frame = Frame(master)
            self.frame.pack()
            self.bframe = Frame(self.frame)
            self.bframe.pack(side=TOP)
            self.gframe = Frame(self.frame, bd=2, relief=RAISED)
            self.g = Canvas(self.gframe, bg='white', width=self.canvas_size[0], height=self.canvas_size[1])
            self.g.pack()
            self.g.bind('<ButtonPress-1>', self.onClick1)  # click 1 (left)
            self.g.bind('<ButtonPress-2>', self.onClick2)  # click 2 (centre)
            self.g.bind('<ButtonPress-3>', self.onClick3)  # click 3 (right)
            self.gframe.pack(side=TOP)
            self.g.delete(ALL)  # clean du canvas
        else:
            self.g = None

    def onClick2(self, event):
        """ On sleep pendant 1 a 60 secondes proportionnel a x, d'un click centre. """
        sleep(int(60 * event.x // self.canvas_size[0]) + 1)

    def onClick1(self, event):
        """ On ralentie l'affichage d'un % proportionnel a x (i.e. 0 a 100%), d'un click left. """
        self.refreshTk *= 1.0 + event.x / self.canvas_size[0]

    def onClick3(self, event):
        """ On accelere l'affichage d'un % proportionnel a x (i.e. 0 a 100%), d'un click right. """
        self.refreshTk *= 0.5 * event.x / self.canvas_size[0]

    def init_modele(self):  # init du modele
        self.nbPas = 4000000  # nombre de pas de simulation
        self.etat = 0  # variable d'etat

    def update(self):  # update du modele
        self.etat = self.etat + 1  # mise a jour de l'etat du modele
        if self.etat % 24 == 0 :
            self.system.computeDailyQty()
        self.system.update()

    def render(self, g):  # rendering du modele dans le canvas Tk g
        bbox = (0, 0, 800, 600)
        g.create_rectangle(bbox, width=1, outline="black", fill="LavenderBlush4")
        bbox = (20, 20, 150, 80)
        g.create_rectangle(bbox, width=1, outline="black", fill="SlateGray")

        tmpDay = self.etat//24
        g.create_text((85, 30), text=str(tmpDay)+"d "+str(self.etat%24)+"h", font=('times', 12), fill='black')
        tmp = self.system.getTrainShip()

        if(tmp[0]):
            g.create_text((85, 50), text="d/train: "+str(round(tmpDay/tmp[0],4)), font=('times', 12), fill='black')
        if(tmp[1]):
            g.create_text((85, 70), text="d/ship: "+str(round(tmpDay/tmp[1],4)), font=('times', 12), fill='black')
        default_width = 110
        default_height = 70
        self.system.render(g,default_width,default_height)

    def run(self):
        ############################################
        # debut boucle de simulation de la dynamique
        for i in range(self.nbPas):
            # on opere le systeme pour un pas
            self.update()

            now = time.time()

            # rendering tkinter
            if now - self.start>config._fps and self.g is not None:
                self.start = now
                self.g.delete(ALL)
                self.render(self.g)
                self.g.update()
                if i == 0: sleep(self.waitTk)  # on attends pour laisser voir l'etat initial
                # fin boucle de simulation de la dynamique
                ############################################
            sleep(self.refreshTk)


""" A executer seulement si ce n'est pas un import, mais bien un run du code. """
if __name__ == '__main__':

    _system = System()
    _system.init_workshop()
    _system.init_transit()
    _system.init_behavior()

    if doRenderTk:  # avec rendering Tk (animation)
        root = Tk()
        root.geometry("+0+0")
        root.title("simulation")
    else:
        root = None
    x = Modele(_system, root)  # creation du modele
    x.run()  # run du modele (simulation) avec ou sans animation
    if root is not None: root.mainloop()
