# Pris en charge de fond coloré, avec une ligne de surface.
# Vue en 2D
# Création du personnage
# Saut non gravitationnel du personnage

from tkinter import *
import time
import random

pos1 = 10 #X
pos2 = 90 #Y
pos3 = 60 #X
pos4 = 140 #Y
jumping = False

fenetre = Tk()
#canvas
canvas = Canvas(fenetre, width=150, height=150, background='orange')

#bonhomme
pnj = canvas.create_oval(pos1, pos2, pos3, pos4)
ligne1 = canvas.create_line(0,140, 150, 140)
##saut du bonhomme
def click(event):
    global jumping
    if jumping == False:
        jump()
        jumping = True

def jump():
    global pos2,pos4
    if pos2 != 60:
        canvas.coords(pnj,pos1,pos2,pos3,pos4)
        pos2 -= 1
        pos4 -= 1
        canvas.after(10,jump)
    else:
        canvas.after(10, fall)

def fall():
    global pos2,pos4, jumping
    if pos2 != 90:
        canvas.coords(pnj,pos1,pos2,pos3,pos4)
        pos2 += 1
        pos4 += 1
        canvas.after(10,fall)
    else:
        jumping = False

fenetre.bind("<space>", click)

#bouton
bouton=Button(fenetre, text="Fermer", command=fenetre.destroy)

#pack
bouton.pack()
canvas.pack()

fenetre.mainloop()
