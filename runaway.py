from tkinter import *
from time import *
from random import *

# Position du personnage
pob1 = 10
pob2 = 130
pob3 = 60
pob4 = 180

# Position du triangle (décor)
pod1 = 450
pod2 = 470
pod3 = 460

# Position du triangle temporaire
pot1 = -1
pot2 = 19
pot3 = 9

# Vitesse de saut et hauteur par ailleurs
inispeed = 10
speed = 10 #la valeur de speed sera changée, et on reviendra à inispeed.

# Variables pour le saut, et l'activiation du décor (au clic droit)
jumping = False
decoractive = False
decortempactive = False

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

#bonhomme
pnj = canvas.create_oval(pob1, pob2, pob3, pob4)
ligne1 = canvas.create_line(0,180, 450, 180)

# #saut du bonhomme
def jump():
    global pob2,pob4, speed
    if speed > 0:
        canvas.coords(pnj,pob1,pob2,pob3,pob4)
        pob2 -= speed
        pob4 -= speed
        speed -= 1
        canvas.after(30,jump)
    else:
        canvas.after(30, fall)

# #redescente du bonhomme
def fall():
    global pob2, pob4, jumping, speed, inispeed
    if speed < inispeed+1:
        canvas.coords(pnj,pob1,pob2,pob3,pob4)
        pob2 += speed
        pob4 += speed
        speed += 1
        canvas.after(30,fall)
    else:
        canvas.coords(pnj,pob1,pob2,pob3,pob4)
        speed = inispeed
        jumping = False

#decor
decor = canvas.create_polygon(pod1, 0, pod2, 0, pod3, 15, fill='blue')
decortemp = canvas.create_polygon(0, 0, 0, 0, 0, 0, fill='blue')
# #déplacement décor
def decordef():
    global decoractive, decortempactive, pod1, pod2, pod3
    if decoractive == True:
        if pod1 != 0:
            canvas.coords(decor, pod1, 0, pod2, 0, pod3, 15)
            pod1 -= 2
            pod2 -= 2
            pod3 -= 2
            canvas.after(10, decordef)
        else:
            pod1 = 450
            pod2 = 470
            pod3 = 460
            pot1 = -1
            pot2 = 19
            pot3 = 9
            decortempactive = True
            canvas.after(10, decortempdef)
            canvas.after(10, decordef)

# # déplacement décor temporaire
def decortempdef():
    global pot1, pot2, pot3, decortempactive
    if decortempactive == True:
        if pot3 != 0:
            canvas.coords(decortemp, pot1, 0, pot2, 0, pot3, 15)
            pot1 -= 1
            pot2 -= 1
            pot3 -= 1
            canvas.after(10, decortempdef)
        else:
            pot1 = -1
            pot2 = 19
            pot3 = 9
            decortempactive = False
            canvas.coords(decortemp, 0, 0, 0, 0, 0, 0)
            canvas.after(10, decortempdef)

#clics et fonctions
# #clic gauche (clickl : clickleft)
def clickl(event):
    global jumping
    if jumping == False:
        jump()
        jumping = True

# #clic droit (clickr: clickright)
def clickr(event):
    global decoractive, decortempactive
    if decortempactive == False:
        if decoractive == False:
            decoractive = True
            decordef()
        else:
            decoractive = False
            decordef()

# # Mise en place des boutons de la souris pour faire les fonctions
fenetre.bind("<Button-1>", clickl)
fenetre.bind("<space>", clickr)

#bouton
bouton=Button(fenetre, text="Fermer", command=fenetre.destroy)

# Programme à Emilien


#sous-programmes


def random_objet(event):  # lancement du programme, generation du type d'obstacle
    global x_objet, random_item, execute
    if execute == 0:
        x_objet = 444
        random_item = int(random()*3)
        defillement()


def defillement():
    global y_objet, x_objet, execute
    if random_item == 0:
        if x_objet > 2:
            execute = 1
            x_objet = x_objet - 2
            canvas.coords(obstacle1, x_objet-7, y_objet+10, x_objet, y_objet)
            canvas.coords(obstacle2, x_objet, y_objet, x_objet+7, y_objet+10)
            fenetre.after(10, defillement)
        if x_objet < 3:
            execute = 0
            canvas.coords(obstacle1, 0, 0, 0, 0)
            canvas.coords(obstacle2, 0, 0, 0, 0)
    if random_item == 1:
        if x_objet > 2:
            execute = 1
            x_objet = x_objet - 2
            canvas.coords(obstacle1, x_objet-7, y_objet+10, x_objet, y_objet)
            canvas.coords(obstacle2, x_objet, y_objet, x_objet+7, y_objet+10)
            canvas.coords(obstacle3, x_objet+7, y_objet, x_objet+7, y_objet+10)
            canvas.coords(obstacle4, x_objet+7, y_objet, x_objet+17, y_objet)
            canvas.coords(obstacle5, x_objet+17, y_objet, x_objet+17, y_objet+10)
            fenetre.after(10, defillement)
        if x_objet < 3:
            execute = 0
            canvas.coords(obstacle1, 0, 0, 0, 0)
            canvas.coords(obstacle2, 0, 0, 0, 0)
            canvas.coords(obstacle3, 0, 0, 0, 0)
            canvas.coords(obstacle4, 0, 0, 0, 0)
            canvas.coords(obstacle5, 0, 0, 0, 0)

    if random_item == 2:
        if x_objet > 2:
            execute = 1
            x_objet = x_objet - 2
            canvas.coords(obstacle1, x_objet-7, y_objet+10, x_objet, y_objet)
            canvas.coords(obstacle2, x_objet, y_objet, x_objet+7, y_objet+10)
            canvas.coords(obstacle3, x_objet+7, y_objet+10, x_objet+14, y_objet)
            canvas.coords(obstacle4, x_objet+14, y_objet, x_objet+21, y_objet+10)
            fenetre.after(10, defillement)
        if x_objet < 3:
            execute = 0
            canvas.coords(obstacle1, 0, 0, 0, 0)
            canvas.coords(obstacle2, 0, 0, 0, 0)
            canvas.coords(obstacle3, 0, 0, 0, 0)
            canvas.coords(obstacle4, 0, 0, 0, 0)

    if len(canvas.find_overlapping(canvas.coords(pnj)[0],canvas.coords(pnj)[1],
    canvas.coords(pnj)[2],canvas.coords(pnj)[3]))>2:
        canvas.coords(pnj, 0,0,0,0)


#obstacles

fenetre.bind("<p>", random_objet)
obstacle1 = canvas.create_line(0, 0, 0, 0)
obstacle2 = canvas.create_line(0, 0, 0, 0)
obstacle3 = canvas.create_line(0, 0, 0, 0)
obstacle4 = canvas.create_line(0, 0, 0, 0)
obstacle5 = canvas.create_line(0, 0, 0, 0)

#pack
bouton.pack()
canvas.pack()

fenetre.mainloop()
