from tkinter import *
import time
import random

# Position du personnage
pob1 = 10
pob2 = 90
pob3 = 60
pob4 = 140

# Position du triangle (décor)
pod1 = 150
pod2 = 170
pod3 = 160

# Position du triangle temporaire
pot1 = -1
pot2 = 19
pot3 = 9

# Variables pour le saut, et l'activiation du décor (au clic droit)
jumping = False
decoractive = False
decortempactive = False

fenetre = Tk()
#canvas
canvas = Canvas(fenetre, width=150, height=150, background='orange')

#bonhomme
pnj = canvas.create_oval(pob1, pob2, pob3, pob4)
ligne1 = canvas.create_line(0,140, 150, 140)

# #saut du bonhomme
def jump():
    global pob2,pob4
    if pob2 != 60:
        canvas.coords(pnj,pob1,pob2,pob3,pob4)
        pob2 -= 1
        pob4 -= 1
        canvas.after(10,jump)
    else:
        canvas.after(10, fall)

# #redescente du bonhomme
def fall():
    global pob2, pob4, jumping
    if pob2 != 90:
        canvas.coords(pnj,pob1,pob2,pob3,pob4)
        pob2 += 1
        pob4 += 1
        canvas.after(10,fall)
    else:
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
            pod1 -= 1
            pod2 -= 1
            pod3 -= 1
            canvas.after(10, decordef)
        else:
            pod1 = 150
            pod2 = 170
            pod3 = 160
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
fenetre.bind("<Button-3>", clickr)

#bouton
bouton=Button(fenetre, text="Fermer", command=fenetre.destroy)

#pack
bouton.pack()
canvas.pack()

fenetre.mainloop()
