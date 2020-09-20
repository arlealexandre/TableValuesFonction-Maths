from tkinter import *
import math

fenetre = Tk()

# CONFIGURATION FENETRE # CONFIGURATION FENETRE # CONFIGURATION FENETRE # CONFIGURATION FENETRE # CONFIGURATION FENETRE

fenetre.title("Tableau de valeurs d'une fonction")
fenetre.geometry('800x400')
fenetre.iconbitmap("maths.ico")
fenetre.minsize(800, 400)

# FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS # FONCTIONS 

def valeurs():

    res_box = LabelFrame(box3,text=str(fx.get()))
    res_box.pack()

    btn_erase = Button(res_box, text="Effacer", command=lambda:[res_box.pack_forget(), btn_erase.pack_forget()])
    btn_erase.pack(side=RIGHT)

    fonction = str(fx.get())
    debut = float(d.get())
    fin = float(f.get())
    pas = float(p.get())

    x = debut

    while (x <= fin):
        fxt = Label(res_box, text="F("+str(x)+") = "+str(eval(fonction)))
        fxt.pack()
        x = x + pas

# AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE # AFFICHAGE 

master = Frame(fenetre)
master.pack(fill=X)

# Box 1 

box1 = Frame(master)
box1.pack()

titre = Label(box1, text="TABLEAU DE VALEURS D'UNE FONCTION", font=(22))
titre.pack(fill=X)

sous_titre = Label(box1, text="Entrez une fonction dont vous voulez connaître les différentes valeurs.\nPrécisez la valeur de départ, celle de fin ainsi que le pas.\nIMPORTANT: Début > Fin, Pas > 0.")
sous_titre.pack(fill=X)

fonction = Label(box1, text="F(x) = ")
fonction.pack(fill=X)

fx = Entry(box1, width=10)
fx.insert(0, "ex: (x*x)/((0.5*x)+1)")
fx.pack(fill=X)

# Box 2

box2 = Frame(master)
box2.pack()

d = Entry(box2, width=10)
d.insert(0, "Début")
d.grid(column=1, row=2, padx=2, pady=10)

f = Entry(box2, width=10)
f.insert(0, "Fin")
f.grid(column=2, row=2, padx=2, pady=2)

p = Entry(box2, width=10)
p.insert(0, "Pas")
p.grid(column=3, row=2, padx=2, pady=2)

btn_side = Button(box2, text="Calculer", width=10, command=valeurs)
btn_side.grid(column=4, row=2, padx=2, pady=2)

# Box 3

box3 = Frame(master)
box3.pack()

fenetre.mainloop()
