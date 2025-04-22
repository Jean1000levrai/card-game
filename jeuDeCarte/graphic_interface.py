import main
import tkinter as tk
from PIL import Image, ImageTk

def charger_image(chemin, nb_image = 1, taille=None ,index_debut = 1, miroir=False, extension = ".png"):
    '''fonction qui sert sert à charger les images. Elle prend en parametre : le chemin d'acces(chemin),
    indice du debut(index_debut) et fin/le nombre d'image(nb_image), un tuple pour la taille de l'image 
    et booléen pour savoir si l'image doit etre tournée ou non
    on utilisera la methode ".extend" pour remplir une liste si besoin'''
    image = []  # crée une liste qui contiendra les images
    for i in range(index_debut, index_debut + nb_image):
        imag = Image.open(chemin + str(i) + extension)
        if taille != None:
            imag = imag.resize(taille)
        if miroir == True:
            imag = imag.transpose(Image.FLIP_LEFT_RIGHT)
        image.append(ImageTk.PhotoImage(imag, master=window))
    return image

def turn():
    '''fonction qui contrôle le fonctionnement du tour avec les comparaisons de cartes,
      lancée par le button "tour"'''
    global score_j1, score_j2, score_j1_text, score_j2_text
    if game.carte_gagne["j1"]+game.carte_gagne["j2"] != 52: #si toutes les cartes ne sont pas encore distribuées
        game.jouer()    # relance un tour
        canvas.itemconfig(img_carte_j1, image=img_carte[game.carte_j1[1]][game.carte_j1[0]-2])
        canvas.itemconfig(img_carte_j2, image=img_carte[game.carte_j2[1]][game.carte_j2[0]-2])
        # actualise le score
        score_j1 = game.carte_gagne['j1']
        score_j2 = game.carte_gagne['j2']
        score_j1_text.config(text=f"score J1 : {score_j1}")
        score_j2_text.config(text=f"score J2 : {score_j2}")
    else:   # si toutes les cartes ont été distribuées
        # affiche le vainqueur à l'écran
        if game.verdict() == 1:
            canvas.create_text(500,350,text="J1 a gagné!", font=("bold", 50), fill="dark blue")
        elif game.verdict() == 2:
            canvas.create_text(500,350,text="J2 a gagné!", font=("bold", 50), fill="dark blue")
        elif game.verdict() == 0:
            canvas.create_text(500,350,text="Egalité!", font=("bold", 50), fill="dark blue")
        else:   # ne se lance jamais, en théorie
            canvas.create_text(500,350,text="BUG DE LA MATRIX!", font=("bold", 50), fill="dark blue")

# -------------code principal---------------
game = main.Bataille()
score_j1 = game.carte_gagne['j1']
score_j2 = game.carte_gagne['j2']

# ------éléments fenêtre------
window = tk.Tk()
window.geometry('1000x700')
canvas = tk.Canvas(window, width=1000, height=600, bg="green")
quit = tk.Button(window, text='Quitter', command = window.destroy)  # on crée un bouton pour quitter le jeu
turnn = tk.Button(window, text='tour', command=turn)

# -----images-----
img_carte = [[],[],[],[],[]]   # pique, trèfle, carreaux, coeur, fonds
# on rempli la liste avec les images en utilisant la fonction charger_image
img_carte[0].extend(charger_image("img/s", 13,index_debut=2,taille=(150,200), extension = ".gif"))
img_carte[1].extend(charger_image("img/c", 13,index_debut=2,taille=(150,200), extension = ".gif"))
img_carte[2].extend(charger_image("img/d", 13,index_debut=2,taille=(150,200), extension = ".gif"))
img_carte[3].extend(charger_image("img/h", 13,index_debut=2,taille=(150,200), extension = ".gif"))
img_carte[4].extend(charger_image("img/bg", taille=(1000,600)))

game.distribuer()

# -----interface------
canvas.create_image(0, 0, anchor=tk.NW, image=img_carte[4][0])
img_carte_j1 = canvas.create_image(300,300,image=None)
img_carte_j2 = canvas.create_image(700,300,image=None)
score_j1_text = tk.Label(window, text="score J1 : ", font='bold')
score_j2_text = tk.Label(window, text="score J2 : ", font='bold')
score_j1_text.pack()
score_j2_text.pack()

canvas.pack()
turnn.pack()
quit.pack()

window.mainloop()