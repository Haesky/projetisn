from tkinter import *
fenetre = Tk()
#canvas

canvas = Canvas(fenetre, width=450, height=200, background='orange')

coo1 = 550
coo2 = 570
x = canvas.create_line(coo1, 180, coo2, 190, coo2, 205)
x = (canvas.coords(x))

decorsolcoor=[0,0,0,0,0,0,0,0,0,0,0,0] #Stock les coordonnées
decorsol = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0] #Stock les objets du canvas

for y in range (1, 12): # Création des objets
    compteur = -1 #le compteur est incrémenté, et défini la position de chaque objet dans les listes
    for i in x:
        compteur += 1
        if x[compteur] not in [1,3,5]: # On ne modifie que les valeurs en x, pas en y
            i -= 50
            x[compteur] = i
    decorsol[y] = canvas.create_line(x[0], 180, x[2], 190, x[4], 205) #On utilise les valeurs de x
    decorsolcoor[y] = (canvas.coords(decorsol[y]))

decorsol[0] = [coo1, 180, coo2, 190, coo2, 205]
decorsolcoor[0] = [coo1, 180, coo2, 190, coo2, 205]


def move():
    global decorsolcoor, compteur, decorsol, compteur2
    if compteur2 < 25: #compteur2 sert à compter le déplacement des lignes
        for item in decorsolcoor: #On utilise decorsol pour les objets, et item pour définir les coordonnées
            item[0] -= 2
            item[2] -= 2
            item[4] -= 2
            canvas.coords(decorsol[compteur], item[0], 180, item[2], 190, item[4], 205)
            compteur += 1 
        compteur = 0 #compteur est incrémenté de 0 à 10, pour prendre toutes les valeurs de la liste decorsol
        compteur2 += 1
        canvas.after(10,move)
    else: #Si compteur2 arrive à 25, du coup on remet les lignes à leurs positions initiales.
        for item in decorsolcoor: 
            item[0] += 48
            item[2] += 48
            item[4] += 48
            canvas.coords(decorsol[compteur], item[0],180, item[2], 190, item[4], 205)
            compteur += 1
        compteur = 0
        compteur2 = 0
        canvas.after(10,move)
            
compteur2 = 0
compteur = 0
canvas.after(10, move)


canvas.create_line(0, 190, 460, 190)
canvas.create_line(0,180,450,180)


canvas.pack()

fenetre.mainloop()
