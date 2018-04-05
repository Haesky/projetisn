from tkinter import *
import time
import random

pob1 = 10 #X
pob2 = 90 #Y
pob3 = 60 #X
pob4 = 140 #Y
pod1 = 150 #Triangle haut gauche
pod2 = 170 #Triangle haut droit
pod3 = 160 #Triangle bas
pot1 = -1
pot2 = 19
pot3 = 9
jumping = False
decoractive = False
decortempactive = False

fenetre = Tk()
#canvas
canvas = Canvas(fenetre, width=150, height=150, background='orange')

#bonhomme
pnj = canvas.create_oval(pob1, pob2, pob3, pob4)
ligne1 = canvas.create_line(0,140, 150, 140)
##saut du bonhomme
def jump():
    global pob2,pob4
    if pob2 != 60:
        canvas.coords(pnj,pob1,pob2,pob3,pob4)
        pob2 -= 1
        pob4 -= 1
        canvas.after(10,jump)
    else:
        canvas.after(10, fall)

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
##déplacement décor
def decordef():
    global decoractive, decortempactive, pod1, pod2, pod3
    if decoractive == True: #PROBLEME
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
            decortempactive = True
            decortempdef()
            canvas.after(10, decordef)
            
def decortempdef():
    global pot1, pot2, pot3, decortempactive #PROBLEME LA AUSSI
    if pot3 != 0:
        canvas.coords(decortemp, pot1, 0, pot2, 0, pot3, 15)
        pot1 -= 1
        pot2 -= 1
        pot3 -= 1
        canvas.after(10, decortempdef)
    else:
        decortempactive = False
        canvas.coords(decortemp, 0, 0, 0, 0, 0, 0)
        canvas.after(10, decortempdef)

#clicks
def clickl(event):
    global jumping
    if jumping == False:
        jump()
        jumping = True
		
def clickr(event):
    global decoractive, decortempactive
    if decortempactive == False:
        if decoractive == False:
            decoractive == True
            # print(decoractive) >> PROBLEME
            decordef()
        else:
            decoractive == False
            decordef()

fenetre.bind("<Button-1>", clickl)
fenetre.bind("<Button-3>", clickr)

#bouton
bouton=Button(fenetre, text="Fermer", command=fenetre.destroy)

#pack
bouton.pack()
canvas.pack()

fenetre.mainloop()
