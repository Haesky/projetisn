from tkinter import *

def run1():
    fenetre.destroy()
    import runaway

def run2():
    fenetre.destroy()
    import fall

fenetre = Tk()

Frame1 = Frame(fenetre)
photo = PhotoImage(file="ressources/runaway.png")
buttonimg = Button(Frame1, image=photo)
buttonimg.grid()
Frame1.grid()

Frame2 = Frame(fenetre)

bouton1 = Button(Frame2, text="Jouer - 1", font="Arial 30", command=run1)
bouton1.grid(row=2, column=1)

bouton2 = Button(Frame2, text="Jouer - 2", font="Arial 30", command=run2)
bouton2.grid(row=2, column=2)

bouton3 = Button(Frame2, text="Fermer", font="Arial 30",command=fenetre.quit)
bouton3.grid(row=2, column=3)
Frame2.grid()

fenetre.mainloop()











