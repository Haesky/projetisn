from tkinter import *
from random import *

fenetre = Tk()
can1 = Canvas(fenetre, width=200, height=200)
obstacle = []
mort = 0


def left(event):
    global x_perso, mort
    if mort == 0:
        x_perso = x_perso - 7
        if x_perso < 0:
            x_perso = 0
        can1.coords(perso, x_perso, 50, x_perso+10, 60)


def right(event):
    global x_perso, mort
    if mort == 0:
        x_perso = x_perso + 7
        if x_perso > 200:
            x_perso = 195
        can1.coords(perso, x_perso, 50, x_perso+10, 60)


def obstacles(event):
    global y_objet, x_objet
    x_objet = int(random()*200)
    y_objet = 200
    obstacle.append(can1.create_line(x_objet-20, 210, 0, 210))
    defillement()


def defillement():
    global y_objet, x_objet
    for objet in obstacle:
        coordonnees = can1.coords(objet)
        if coordonnees[2] < 0:
            del obstacle[0]
            objet = 1
        else:
            can1.coords(
                objet, coordonnees[0]-2, coordonnees[1], coordonnees[2]-2, coordonnees[3])
    fenetre.after(10, defillement)


def test_mort():
    global x_perso, x_objet, mort
    if x_perso < x_objet - 20 or x_perso > x_objet + 20:
        mort = 1
        x_perso = 250
        can1.coords(perso, x_perso, 50, x_perso+10, 60)


def respawn(event):
    global mort, x_perso
    mort = 0
    print("test")
    x_perso = 100
    can1.coords(perso, x_perso, 50, x_perso+10, 60)


can1.pack()
fenetre.bind("<Left>", left)
fenetre.bind("<Right>", right)
fenetre.bind("<Return>", obstacles)
fenetre.bind("<Up>", respawn)
fenetre.mainloop()
