##################
# initialisation #
##################

#importation des modules :
from tkinter import *
from time import *
from random import *


#############
# variables #
#############
# Position du personnage
pob1 = 20
pob2 = 135
pob3 = 70
pob4 = 185

obstacle = []
flag = 0

# Couleur du décor
colordecor = "#AB6300"

#Décor sol
coo1 = 550
coo2 = 570
decorsolcoor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Stock les coordonnées
decorsol = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Stock les objets du canvas
compteur2 = 0 # Ce compteur nous permet de voir quand on replace le décor du sol.

# Position du décor
pod1 = 450
pod2 = 500
pod3 = 490
pod4 = 460

# Difficulté qui augmente au fur et à mesure
dif = 2.5

# Variable qui détecte la fin
finish = False

# Vitesse de saut et hauteur par ailleurs
inispeed = 8
speed = 8 #la valeur de speed sera changée, et on reviendra à inispeed.

# Variables pour le saut, et l'activiation du décor (au clic droit)
jumping = 0

# Score en fin de jeu
score = 0

# Variables a Emilien
x_objet = 444
y_objet = 170
## ces deux variables vont agir dans les coordonnées de l'obstacle. elles sont lourdes et devrait etre stocke dans une liste
random_item = 0
## me permet de generer un type d'obstacle aleatoirement
execute = 0
## me permet de vérifier que le programme ne s'execute pas deux fois en meme temps.

#######################
# Interface graphique #
#######################

fenetre = Tk()

#canvas
canvas = Canvas(fenetre, width=450, height=200, background='orange')

#decor
decor = canvas.create_polygon(pod1, 1, pod2, 1, pod3, 15, pod3, 180, pod4, 180, pod4, 15, fill='orange', outline='black', width='1')

x = canvas.create_line(coo1, 180, coo2, 190, coo2,205)  # la variable x permet de créer les lignes aux sols
x = (canvas.coords(x)) #En reprenant la création de la ligne, on pourra modifier plus tard avec des fonctions les positions des tous les traits.

#bonhomme
pnj = canvas.create_oval(pob1, pob2, pob3, pob4,fill='orange')

#lignes aux sols (qui sont stables)
ligne1 = canvas.create_line(0,180, 450, 180) # 1ère ligne 
ligne2 = canvas.create_line(0,3,460,3) # Servira pour créer les différents traits
ligne3 = canvas.create_line(0, 190, 460, 190) #2ème ligne

#############
# Fonctions #
#############

#saut du bonhomme
def jump():
    global pob2,pob4, speed, jumping
    if jumping == 1 : # On regarde si le bonhomme saute déjà
        if speed > 0: # Si la vitesse n'a pas atteind 0, on continue de faire baisser la vitesse
            canvas.coords(pnj,pob1,pob2,pob3,pob4)
            pob2 -= speed # On change les positions en y du personnage, en fonction de la vitesse
            pob4 -= speed 
            speed -= 0.5 # On change la vitesse.
            canvas.after(10,jump)
        else:
            canvas.after(10, fall) # Si on a atteind l'apogée du saut, on met le bonhomme en retombée

#redescente du bonhomme. Le principe est le même que le saut, mais dans le sens inverse
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
            pob2=135 # Si jamais le bonhomme retombe trop vite (avec une vitesse de 8 par exemple), normalement
            pob4=185 # il devrait être au-dessous des lignes. On recadre ça en reprenant ses positions initiales.
            canvas.coords(pnj,pob1,pob2,pob3,pob4)
            speed = inispeed # On réinitialise la vitesse.
            jumping -= 1 # On enlève le fait que le bonhomme était en train de sauter.

# double saut du bonhomme

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
    global jumping, speed, pob2, pob4, finish
    # Comme le doublefall dépend des positions du pnj, si le joueur fait une double descente sur un piège il perd
    # Du coup comme il n'y a plus de coordonnées, cela engendres des soucis. On vérifie si le jeu est fini avec la
    # variable finish.
    if finish == False:
        if (canvas.coords(pnj)[0], canvas.coords(pnj)[1], canvas.coords(pnj)[2], canvas.coords(pnj)[3]) < (20.0, 135, 70, 185):
            # Ici, on utilisera cette fonction pour détecter si le bonhomme dépasse la ligne. Si oui, on le remettra à ses coordonnées
            # initiales.
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

# #déplacement décor du pilier
def decordef():
    global pod1, pod2, pod3, pod4, score
    if pod2 > 0:
        canvas.coords(decor, pod1, 3, pod2, 3, pod3, 15, pod3, 180, pod4, 180, pod4, 15,)
        pod1,pod2,pod3,pod4 = pod1-dif,pod2-dif,pod3-dif,pod4-dif #On fait évoluer le pilier en fonction de la variable "dif"
        canvas.after(10, decordef)
    else: # Quand le pilier arrive au bout du canvas, on réinitialise ses coordonnées.
        pod1 = 450
        pod2 = 500
        pod3 = 490
        pod4 = 460
        # En même temps, c'est ici qu'on augmentera le score. (On aurait pu le mettre autrepart)
        score += 100
        canvas.after(10, decordef)

for y in range(1, 12):  # Création des objets
    compteur = -1  # le compteur est incrémenté, et défini la position de chaque objet dans les listes
    for i in x: # Comme dit précedemment, la variable x contient les coordonnées du premier trait sur le sol.
        compteur += 1
        if x[compteur] not in [1, 3, 5]:  # On ne modifie que les valeurs en x, pas en y
            i -= 50
            x[compteur] = i
    decorsol[y] = canvas.create_line(
        x[0], 180, x[2], 190, x[4], 205)  # On utilise les valeurs modifiées pour créer nos traits espacés
    decorsolcoor[y] = (canvas.coords(decorsol[y])) # On stock les coordonnées des nouveaux traits dans la variable decorsolcoor

decorsol[0] = [coo1, 180, coo2, 190, coo2, 205] #Comme on a fait "for y in range (1,12)", le 1er élément de la liste n'est pas défini.
decorsolcoor[0] = [coo1, 180, coo2, 190, coo2, 205] # Du coup on le fait manuellement pour decorsol et decorsolcoor
 
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
            canvas.coords(decorsol[compteur], item[0],180, item[2], 190, item[4], 205)
            compteur += 1
        compteur = 0
        compteur2 = 0
        canvas.after(10, move)

compteur = 0 # Cette variable est une exception, et on est obliger de la placer là sans quoi le programme ne fonctionne pas.

# boutton espace, pour sauter ou doublesauter
def space(event):
    global jumping, speed
    if jumping == 0: #Si on n'a pas encore sauté, alors on saute 1 fois
        jumping += 1
        jump()
    elif jumping == 1: # Sinon, si il y a déjà un saut d'actif, on active le double saut.
        jumping += 1
        speed = inispeed
        doublejump()

# Programme à Emilien

#sous-programmes

## installe un temps entre chaque obstacle
def generation():
    go = int(random()*100)
    if go != 1:
        fenetre.after(1000, generation)
    random_objet()

## Puis genere un type d'obstacle...
def random_objet(): 
    global random_item
    random_item = int(random()*22)
    new_objet()

## ...Et le cree
def new_objet():
    global flag, finish
    if finish == False:
        if 1<random_item< 5:
            obstacle.append(canvas.create_line(450, 185, 465, 165))
            obstacle.append(canvas.create_line(465, 165, 480, 185))
        if 6<random_item< 10:
            obstacle.append(canvas.create_line(450, 185, 465, 165))
            obstacle.append(canvas.create_line(465, 165, 480, 185))
            obstacle.append(canvas.create_line(480, 185, 495, 165))
            obstacle.append(canvas.create_line(495, 165, 510, 185))
        if 11<random_item< 15:
            obstacle.append(canvas.create_line(450, 185, 465, 165))
            obstacle.append(canvas.create_line(465, 165, 480, 185))
            obstacle.append(canvas.create_line(480, 185, 480, 165))
            obstacle.append(canvas.create_line(480, 165, 500, 165))
            obstacle.append(canvas.create_line(500, 165, 500, 185))
        if 16<random_item< 20:
            obstacle.append(canvas.create_line(480, 165, 490, 150))
            obstacle.append(canvas.create_line(490, 150, 500, 165))
            obstacle.append(canvas.create_line(480, 185, 480, 165))
            obstacle.append(canvas.create_line(480, 165, 500, 165))
            obstacle.append(canvas.create_line(500, 165, 500, 185))
        if flag == 0:
            defillement()
            flag = 1

## Enfin, l'obstacle se met à bouger
def defillement():
    global y_objet, x_objet, finish
    if finish == False:
        for objet in obstacle:
            coordonnees = canvas.coords(objet)
            if coordonnees[2] < -50:
                del obstacle[0]
                objet = 1
            else:
                canvas.coords(
                    objet, coordonnees[0]-dif, coordonnees[1], coordonnees[2]-dif, coordonnees[3])
        # On regarde si les pièges touche le personnage grâce à find_overlapping, qui détecte les élements qui se touchent entre eux.
        mort = (canvas.find_overlapping(canvas.coords(pnj)[0], canvas.coords(pnj)[1], canvas.coords(pnj)[2], canvas.coords(pnj)[3]))
        mortlist = list(mort)
        for i in range(0, 18):
            if i in mortlist:
                mortlist.remove(i) # On enlève tous les éléments susceptibles de toucher le personnage, hors pièges.
        if len(mortlist) != 0:   # On regarde, après avoir enlever tous les éléments si la il y en a encore dans la liste, si oui:
            finish = True        # cela veut dire que la liste contient des pièges, donc que le joueur touche un piège.
            canvas.delete("all") # Du coup on met en place la manoeuvre de fin.
            fin()
        else:
            fenetre.after(10, defillement)

def fin():
    fenetre.destroy()
    print ("Votre score est de",score,"points.")

########
# main #
########

#Appel des fonctions de génération automatique de décor/piège
generation()
decordef()
move()

#Mise en place de la touche espace pour faire une action (sauter)
fenetre.bind("<space>", space)

#bouton
bouton=Button(fenetre, text="Fermer", command=fenetre.destroy)

#pack
bouton.pack()
canvas.pack()

#permet de définir la position (au-dessous ou au-dessus de l'élément spécifié)
for i in range (1,17): 
    canvas.tag_raise(pnj,i) #Ici, le personnage sera au-dessous de tous les éléments. (Sans compter les pièges)

fenetre.mainloop()
