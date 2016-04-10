""" Renderin d'un modele avec Tkinter. """
from System import System
from tkinter import *
from time import sleep

doRenderTk = True  # choix de faire un rendering Tk ou pas


class Modele(object):
    """ Modele pour simulation. """

    def __init__(self, system, master=None):
        self.system = system
        self.init_modele()  # init du modele lui-meme
        # canvas pour le rendering graphique
        self.canvas_size = (600, 600)  # taille du canvas pour le rendering
        if master is not None:  # fenetre de rendering si necessaire
            self.refreshTk = 1.0
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
        self.nbPas = 5  # nombre de pas de simulation
        self.etat = 0  # variable d'etat

    def update(self):  # update du modele
        self.etat = self.etat + 1  # mise a jour de l'etat du modele

    def render(self, g):  # rendering du modele dans le canvas Tk g
        bfont = ('times', 14, 'bold')
        default_width = 150
        default_height = 70

        # UNLOADING DOCK
        unload_top_left_corner = {"x": 50, "y": 50}
        bbox = (unload_top_left_corner["x"], unload_top_left_corner["y"], unload_top_left_corner["x"] + default_width,
                unload_top_left_corner["y"] + default_height)
        unloading_dock = self.system.workshops[0]
        g.create_rectangle(bbox, width=1, outline="black", fill="yellow")
        g.create_text((bbox[0] + default_width/2, bbox[1] + 20), text=str(unloading_dock.name), font=bfont, fill='black')

        # MIXER
        mixer_top_left_corner = {"x": 250, "y": 100}
        bbox = (mixer_top_left_corner["x"], mixer_top_left_corner["y"], mixer_top_left_corner["x"] + default_width,
                mixer_top_left_corner["y"] + default_height)
        mixer = self.system.workshops[1]
        g.create_rectangle(bbox, width=1, outline="black", fill="yellow")
        g.create_text((bbox[0] + default_width/2, bbox[1] + 20), text=str(mixer.name), font=bfont, fill='black')

        # Graphical link between unloading dock and mixer. No storage there ?
        g.create_line(unload_top_left_corner["x"] + default_width, unload_top_left_corner["y"] + default_height/2,
                      mixer_top_left_corner["x"], mixer_top_left_corner["y"] + default_height/2, width=2, fill="orange")

        # MINE
        mine_top_left_corner = {"x": 50, "y": 350}
        bbox = (mine_top_left_corner["x"], mine_top_left_corner["y"], mine_top_left_corner["x"] + default_width,
                mine_top_left_corner["y"] + default_height)
        mine = self.system.workshops[2]
        g.create_rectangle(bbox, width=1, outline="black", fill="yellow")
        g.create_text((bbox[0] + default_width/2, bbox[1] + 20), text=str(mine.name), font=bfont, fill='black')

        # ORE PROCESSING
        process_top_left_corner = {"x": 250, "y": 350}
        bbox = (process_top_left_corner["x"], process_top_left_corner["y"], process_top_left_corner["x"] + default_width,
                process_top_left_corner["y"] + default_height)
        processing = self.system.workshops[3]
        g.create_rectangle(bbox, width=1, outline="black", fill="yellow")
        g.create_text((bbox[0] + default_width/2, bbox[1] + 20), text=str(processing.name), font=bfont, fill='black')

        # Graphical link between mine and ore processing. Missing storage info.
        g.create_line(mine_top_left_corner["x"] + default_width, mine_top_left_corner["y"] + default_height/2,
                      process_top_left_corner["x"], process_top_left_corner["y"] + default_height/2, width=2, fill="orange")

        # Graphical link between mixer and ore processing. Missing storage info.
        g.create_line(mixer_top_left_corner["x"] + default_width/2, mixer_top_left_corner["y"] + default_height,
                      process_top_left_corner["x"] + default_width/2, process_top_left_corner["y"], width=2, fill="orange")

        # LOADING DOCK
        load_top_left_corner = {"x": 450, "y": 350}
        bbox = (load_top_left_corner["x"], load_top_left_corner["y"], load_top_left_corner["x"] + default_width,
                load_top_left_corner["y"] + default_height)
        loading_dock = self.system.workshops[4]
        g.create_rectangle(bbox, width=1, outline="black", fill="yellow")
        g.create_text((bbox[0] + default_width/2, bbox[1] + 20), text=str(loading_dock.name), font=bfont, fill='black')

        # Graphical link between ore processing and loading dock. Missing storage info.
        g.create_line(process_top_left_corner["x"] + default_width, process_top_left_corner["y"] + default_height/2,
                      load_top_left_corner["x"], load_top_left_corner["y"] + default_height/2, width=2, fill="orange")

    def run(self):
        ############################################
        # debut boucle de simulation de la dynamique
        for i in range(self.nbPas):
            # on opere le systeme pour un pas
            self.update()
            # rendering tkinter
            if self.g is not None:
                self.g.delete(ALL)
                self.render(self.g)
                self.g.update()
                sleep(self.refreshTk)
                if i == 0: sleep(self.waitTk)  # on attends pour laisser voir l'etat initial
                # fin boucle de simulation de la dynamique
                ############################################


""" A executer seulement si ce n'est pas un import, mais bien un run du code. """
if __name__ == '__main__':

    _system = System()
    _system.init_behaviour_trees()
    _system.init_workshop()
    _system.init_transit()

    if doRenderTk:  # avec rendering Tk (animation)
        root = Tk()
        root.geometry("+0+0")
        root.title("simulation")
    else:
        root = None
    x = Modele(_system, root)  # creation du modele
    x.run()  # run du modele (simulation) avec ou sans animation
    if root is not None: root.mainloop()
