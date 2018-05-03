#cree par emilien, le 28/03/18 en python 3.2

#importation des modules
from tkinter import *
from time import *
from random import *

#creation des variables
fenetre = Tk()
can1 = Canvas(fenetre, height = 200, width = 200)
x_objet = 194
y_objet = 140
## ces deux variables vont agir dans les coordonnées de l'obstacle. elles sont lourdes et devrait etre stocke dans une liste
random_item = 0
## me permet de generer un type d'obstacle aleatoirement
execute = 0
## me permet de vérifier que le programme ne s'execute pas deux fois en meme temps.

#sous-programmes
def random_objet (event): ## lancement du programme, generation du type d'obstacle
    global x_objet, random_item, execute
    if execute == 0:
        x_objet = 194
        random_item = int(random()*3)
        print(random_item)
        defillement()

def defillement ():
    global y_objet, x_objet, execute
    if random_item == 0:
        if x_objet > 2 :
            execute = 1
            x_objet = x_objet - 2
            can1.coords(obstacle1,x_objet-7,y_objet+10,x_objet,y_objet)
            can1.coords(obstacle2,x_objet,y_objet,x_objet+7,y_objet+10)
            fenetre.after(10, defillement)
        if  x_objet < 3:
            execute = 0
            can1.coords(obstacle1,0,0,0,0)
            can1.coords(obstacle2,0,0,0,0)
    if random_item == 1:
        if x_objet > 2 :
            execute = 1
            x_objet = x_objet - 2
            can1.coords(obstacle1,x_objet-7,y_objet+10,x_objet,y_objet)
            can1.coords(obstacle2,x_objet,y_objet,x_objet+7,y_objet+10)
            can1.coords(obstacle3,x_objet+7,y_objet,x_objet+7,y_objet+10)
            can1.coords(obstacle4,x_objet+7,y_objet,x_objet+17,y_objet)
            can1.coords(obstacle5,x_objet+17,y_objet,x_objet+17,y_objet+10)
            fenetre.after(10, defillement)
        if  x_objet < 3:
            execute = 0
            can1.coords(obstacle1,0,0,0,0)
            can1.coords(obstacle2,0,0,0,0)
            can1.coords(obstacle3,0,0,0,0)
            can1.coords(obstacle4,0,0,0,0)
            can1.coords(obstacle5,0,0,0,0)

    if random_item == 2:
        if x_objet > 2 :
            execute = 1
            x_objet = x_objet - 2
            can1.coords(obstacle1,x_objet-7,y_objet+10,x_objet,y_objet)
            can1.coords(obstacle2,x_objet,y_objet,x_objet+7,y_objet+10)
            can1.coords(obstacle3,x_objet+7,y_objet+10,x_objet+14,y_objet)
            can1.coords(obstacle4,x_objet+14,y_objet,x_objet+21,y_objet+10)
            fenetre.after(10, defillement)
        if  x_objet < 3:
            execute = 0
            can1.coords(obstacle1,0,0,0,0)
            can1.coords(obstacle2,0,0,0,0)
            can1.coords(obstacle3,0,0,0,0)
            can1.coords(obstacle4,0,0,0,0)

#main
can1.create_line (0, 150, 200, 150)
fenetre.bind("<Return>", random_objet)
obstacle1 = can1.create_line (0, 0, 0, 0)
obstacle2 = can1.create_line (0, 0, 0, 0)
obstacle3 = can1.create_line (0, 0, 0, 0)
obstacle4 = can1.create_line (0, 0, 0, 0)
obstacle5 = can1.create_line (0, 0, 0, 0)
can1.pack()

fenetre.mainloop()
