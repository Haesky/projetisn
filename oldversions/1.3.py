from tkinter import *
from time import *
from random import *

# Position du personnage
pob1 = 10
pob2 = 135
pob3 = 60
pob4 = 185

# Couleur du décor
colordecor = "#AB6300"

#Décor sol
coo1 = 550
coo2 = 570
decorsolcoor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Stock les coordonnées
decorsol = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Stock les objets du canvas

# Position du décor
pod1 = 450
pod2 = 500
pod3 = 490
pod4 = 460

# Difficulté qui augmente au fur et à mesure
dif = 3

# Variable qui détecte la fin
finish = False

# Vitesse de saut et hauteur par ailleurs
inispeed = 8
speed = 8 #la valeur de speed sera changée, et on reviendra à inispeed.

# Variables pour le saut, et l'activiation du décor (au clic droit)
jumping = 0

# Variables a Emilien
x_objet = 444
y_objet = 170
## ces deux variables vont agir dans les coordonnées de l'obstacle. elles sont lourdes et devrait etre stocke dans une liste
random_item = 0
## me permet de generer un type d'obstacle aleatoirement
execute = 0
## me permet de vérifier que le programme ne s'execute pas deux fois en meme temps.

fenetre = Tk()
#canvas
canvas = Canvas(fenetre, width=450, height=200, background='orange')
#decor
decor = canvas.create_polygon(pod1, 1, pod2, 1, pod3, 15, pod3, 180, pod4, 180, pod4, 15, fill='orange', outline='black', width='1')
x = canvas.create_line(coo1, 180, coo2, 190, coo2,205)  # créé la 2ème ligne du sol
x = (canvas.coords(x))
#bonhomme
pnj = canvas.create_oval(pob1, pob2, pob3, pob4,fill='orange')
ligne1 = canvas.create_line(0,180, 450, 180)
ligne2 = canvas.create_line(0,3,460,3)

# #saut du bonhomme
def jump():
    global pob2,pob4, speed, jumping
    if jumping == 1 :
        if speed > 0:
            canvas.coords(pnj,pob1,pob2,pob3,pob4)
            pob2 -= speed
            pob4 -= speed
            speed -= 0.5
            canvas.after(10,jump)
        else:
            canvas.after(10, fall)

# #redescente du bonhomme
def fall():
    global pob2, pob4, jumping, speed
    if jumping == 1:
        if speed < inispeed+0.5:
            canvas.coords(pnj,pob1,pob2,pob3,pob4)
            pob2 += speed
            pob4 += speed
            speed += 0.5
            canvas.after(10,fall)
        else:
            pob2=135
            pob4=185
            canvas.coords(pnj,pob1,pob2,pob3,pob4)
            speed = inispeed
            jumping -= 1

# #déplacement décor
def decordef():
    global pod1, pod2, pod3, pod4
    if pod2 > 0:
        canvas.coords(decor, pod1, 3, pod2, 3, pod3, 15, pod3, 180, pod4, 180, pod4, 15,)
        pod1,pod2,pod3,pod4 = pod1-dif,pod2-dif,pod3-dif,pod4-dif
        canvas.after(10, decordef)
    else:
        pod1 = 450
        pod2 = 500
        pod3 = 490
        pod4 = 460
        canvas.after(10, decordef)

canvas.after(10,decordef)

# #décor au sol

for y in range(1, 12):  # Création des objets
    compteur = -1  # le compteur est incrémenté, et défini la position de chaque objet dans les listes
    for i in x:
        compteur += 1
        if x[compteur] not in [1, 3, 5]:  # On ne modifie que les valeurs en x, pas en y
            i -= 50
            x[compteur] = i
    decorsol[y] = canvas.create_line(
        x[0], 180, x[2], 190, x[4], 205)  # On utilise les valeurs de x
    decorsolcoor[y] = (canvas.coords(decorsol[y]))

decorsol[0] = [coo1, 180, coo2, 190, coo2, 205]
decorsolcoor[0] = [coo1, 180, coo2, 190, coo2, 205]

compteur2 = 0

def move():
    global decorsolcoor, compteur, decorsol, compteur2
    if compteur2 < 25:  # compteur2 sert à compter le déplacement des lignes
        for item in decorsolcoor:  # On utilise decorsol pour les objets, et item pour définir les coordonnées
            item[0] -= 2
            item[2] -= 2
            item[4] -= 2
            canvas.coords(decorsol[compteur], item[0],
                          180, item[2], 190, item[4], 205)
            compteur += 1
        compteur = 0  # compteur est incrémenté de 0 à 10, pour prendre toutes les valeurs de la liste decorsol
        compteur2 += 1
        canvas.after(10, move)
    else:  # Si compteur2 arrive à 25, du coup on remet les lignes à leurs positions initiales.
        for item in decorsolcoor:
            item[0] += 50
            item[2] += 50
            item[4] += 50
            canvas.coords(decorsol[compteur], item[0],
                          180, item[2], 190, item[4], 205)
            compteur += 1
        compteur = 0
        compteur2 = 0
        canvas.after(10, move)

compteur = 0
canvas.after(10, move)

ligne2 = canvas.create_line(0, 190, 460, 190)

#clics et fonctions
# #clic gauche (clickl : clickleft)
def saut(event):
    global jumping, speed
    if jumping == 0:
        jumping += 1
        jump()
    elif jumping == 1:
        jumping += 1
        speed = inispeed
        doublejump()

def doublejump():
    global jumping, speed, pob2, pob4
    if speed > 0:
        canvas.coords(pnj, pob1, pob2, pob3, pob4)
        pob2 -= speed
        pob4 -= speed
        speed -= 0.5
        canvas.after(10, doublejump)
    else:
        canvas.after(10, doublefall)

def doublefall():
    global jumping, speed, pob2, pob4
    if (canvas.coords(pnj)[0], canvas.coords(pnj)[1], canvas.coords(pnj)[2], canvas.coords(pnj)[3]) < (10.0, 135, 60, 185):
    #if (canvas.find_overlapping(10, 135, 60, 185))[1] != 14: # (3,4) not in 4 ?
        canvas.coords(pnj, pob1, pob2, pob3, pob4)
        pob2 += speed
        pob4 += speed
        speed += 0.5
        canvas.after(10, doublefall)
    else:
        pob2 = 135
        pob4 = 185
        canvas.coords(pnj, pob1, pob2, pob3, pob4)
        speed = inispeed
        jumping = 0

# # Mise en place des boutons de la souris pour faire les fonctions
fenetre.bind("<space>", saut)

#bouton
bouton=Button(fenetre, text="Fermer", command=fenetre.destroy)

# Programme à Emilien

#sous-programmes

def generation():
    go = int(random()*100)
    if go != 1:
        fenetre.after(1000, generation)
    random_objet()


def random_objet():  # lancement du programme, generation du type d'obstacle
    global random_item
    random_item = int(random()*5)
    new_objet()


def new_objet():
    global flag, finish
    if finish == False:
        if random_item == 0: #x1,y1,x2,y2
            obstacle.append(canvas.create_line(210, 150, 217, 140))
            obstacle.append(canvas.create_line(217, 140, 224, 150))
        if random_item == 1:
            obstacle.append(canvas.create_line(210, 150, 217, 140))
            obstacle.append(canvas.create_line(217, 140, 224, 150))
            obstacle.append(canvas.create_line(224, 150, 231, 140))
            obstacle.append(canvas.create_line(231, 140, 238, 150))
        if random_item == 2:
            obstacle.append(canvas.create_line(210, 150, 217, 140))
            obstacle.append(canvas.create_line(217, 140, 224, 150))
            obstacle.append(canvas.create_line(224, 150, 224, 140))
            obstacle.append(canvas.create_line(224, 140, 234, 140))
            obstacle.append(canvas.create_line(234, 140, 234, 150))
        if random_item == 3:
            obstacle.append(canvas.create_line(210, 150, 210, 140))
            obstacle.append(canvas.create_line(210, 140, 220, 140))
            obstacle.append(canvas.create_line(220, 140, 220, 150))
            obstacle.append(canvas.create_line(209, 140, 215, 130))
            obstacle.append(canvas.create_line(215, 130, 221, 140))
        if flag == 0:
            defillement()
            flag = 1


def defillement():
    global y_objet, x_objet, finish
    if finish == False:
        for objet in obstacle:
            coordonnees = canvas.coords(objet)
            if coordonnees[2] < 0:
                del obstacle[0]
                objet = 1
            else:
                canvas.coords(
                    objet, coordonnees[0]-2, coordonnees[1], coordonnees[2]-2, coordonnees[3])
        mort = (canvas.find_overlapping(canvas.coords(pnj)[0], canvas.coords(pnj)[1], canvas.coords(pnj)[2], canvas.coords(pnj)[3]))
        mortlist = list(mort)
        for i in range(0, 18):
            if i in mortlist:
                mortlist.remove(i)
        if len(mortlist) != 0:
            finish = True
            canvas.delete("all")
        else:
            fenetre.after(10, defillement)



#main
obstacle = []
flag = 0
generation()

#pack
bouton.pack()
canvas.pack()

#permet de définir la position (au-dessous ou au-dessus de l'élément spécifié)
canvas.tag_raise(pnj, decor)
canvas.tag_raise(pnj,ligne2)

fenetre.mainloop()
