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
nombre_obstacles = 0
dif = 2

#sous-programmes
def generation () :
    go = int(random()*100)
    if go != 1 :
        fenetre.after(1000, generation)
    random_objet()

def random_objet (): ## lancement du programme, generation du type d'obstacle
    global x_objet, random_item
    x_objet = 194
    random_item = int(random()*5)
    new_objet()


def new_objet () :
    global flag
    if random_item == 0 :
        obstacle.append(can1.create_line (210,150,217,140))
        obstacle.append(can1.create_line (217,140,224,150))
    if random_item == 1 :
        obstacle.append(can1.create_line (210,150,217,140))
        obstacle.append(can1.create_line (217,140,224,150))
        obstacle.append(can1.create_line (224,150,231,140))
        obstacle.append(can1.create_line (231,140,238,150))
    if random_item == 2 :
        obstacle.append(can1.create_line (210,150,217,140))
        obstacle.append(can1.create_line (217,140,224,150))
        obstacle.append(can1.create_line (224,150,224,140))
        obstacle.append(can1.create_line (224,140,234,140))
        obstacle.append(can1.create_line (234,140,234,150))
    if random_item == 3 :
        obstacle.append(can1.create_line (210,150,210,140))
        obstacle.append(can1.create_line (210,140,220,140))
        obstacle.append(can1.create_line (220,140,220,150))
        obstacle.append(can1.create_line (209,140,215,130))
        obstacle.append(can1.create_line (215,130,221,140))
    if flag == 0:
        defillement()
        flag = 1

def defillement ():
    global y_objet, x_objet
    for objet in obstacle:
        coordonnees = can1.coords(objet)
        if coordonnees[2]<0:
            del obstacle[0]
            objet = 1
        else :
            can1.coords(objet,coordonnees[0]-2,coordonnees[1],coordonnees[2]-2,coordonnees[3])
    fenetre.after(10, defillement)

#main
obstacle = []
flag = 0
can1.create_line (0, 150, 200, 150)
generation()
can1.pack()
fenetre.mainloop()
