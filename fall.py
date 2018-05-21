#Importation des modules
from tkinter import *
from random import *

#Creation d'un interface graphique
fenetre = Tk()
canvas = Canvas(fenetre, width=200, height=250, background = 'orange')

#ariables
mort = 0 ##Defini l'etat du personnage
x_perso = 100 ##coordonnees du personnage
y_perso = 0
y_objet = 0 ## coordonnees des obstacles
x_objet = 0
obstacle1 = canvas.create_oval(0, 0, 0, 0) ## ligne permetant de tracer les obstacles
obstacle2 = canvas.create_oval(0, 0, 0, 0)
perso = canvas.create_oval(x_perso, 50, x_perso+10, 60) ## et rond permettant de tracer le personnage
execute = 0 ## variable qui evite de lancer defilement deux fois
mode = 0 ## Variable, qui était cense defnir le mode de jeu
score = 0 ## score

#Sous programmes
## Pour aller a droite
def left(event):
    global x_perso, mort
    if mort == 0 :
        x_perso = x_perso - 7
        if x_perso < 0 :
            x_perso = 0
        canvas.coords(perso, x_perso, 50, x_perso+10, 60)
## Et a gauche
def right(event):
    global x_perso, mort
    if mort == 0 :
        x_perso = x_perso + 7
        if x_perso > 200 :
            x_perso = 195
        canvas.coords(perso, x_perso, 50, x_perso+10, 60)
## cree un "x" aléatoire, et des obstacles avec ce "x"
def obstacles () :
    global y_objet, x_objet, execute, mode, score, mort
    if mort == 0 : ## Si mort vaut 1, alors le personnage est mort; pas de nouveaux obstacles.
        test = int(random()*10) ## A la base, pour le changement de mode de jeu.
        if test == 1 :
            mode = 0
        if execute == 0 : ## Pour verifier que le programme ne s'est pas lance deux fois
            x_objet = int(random()*200)
            score += 100 ## augmente le score
            y_objet = 250 ## reinitialise le "y" de l'objet pour le placer en dessous
            defilement()

def defilement () :
    global y_objet, x_objet, execute
    y_objet -= 2 ## diminue la valeur de "y" pour cree le mouvement
    execute = 1 ## informe le reste du programme qu'il est deja en cours d'utilisation
    if y_objet > 1 :
        canvas.coords(obstacle1, x_objet - 20, y_objet, 0, y_objet) ## actualise les obstacles
        canvas.coords(obstacle2, x_objet + 20, y_objet, 200, y_objet)
        fenetre.after(10, defilement)
    else : ## une fois l'obstacle arrive au bout, on informe que le programme est a nouveau utilisable
        execute= 0
        if mode == 0 :
            obstacles()
    if y_objet == 56 : ## une fois arrive au niveau du personnage, appelle la fonction qui test si le personnage doit mourir
        test_mort()

def test_mort ():
    global x_perso, x_objet, mort, score
    if x_perso < x_objet - 20 or x_perso > x_objet + 20: ## si le personnage ne se trouve pas dans l'ouverture des deux lignes
        print("vortre score :") ## informe le joueur de son score, puis le supprime
        print(score)
        score = 0
        mort = 1
        x_perso = 250 ## fait disparaitre le personnage en le plaçant hors du canvas
        canvas.coords(perso, x_perso, 50, x_perso+10, 60)

#MAIN
fenetre.bind("<Left>", left)
fenetre.bind("<Right>", right)
obstacles()
canvas.pack()
fenetre.mainloop()
