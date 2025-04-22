import random

class Jeu_de_carte:
    """
    c'est objet : un jeu de carte. il est plein de base
    il comporte 2 paramètre : 
    - empty --> pour avoir un jeu vide ou non
    -  nb_carte --> pour savoir le nombre de carte du jeu

    3 méthodes:
    - nom_carte --> renvoie le nom de la carte donné en paramètre
    - battre --> mélange le jeu de façon aléatoire
    - tirer --> pioche la première carte du paquet
    """
    def __init__(self, empty = False, nb_carte = 52):
        self.nombre_carte = nb_carte   # le nombre de carte(le jeu est vide de base)
        self.pioche = []        # liste contenant toutes les cartes
        if empty == False:      # si le jeu n'est pas vide
        # rempli le jeu
            for i in range(2, self.nombre_carte//4+2):  
            # il y a 4 enseignes et on commence au rang 2 pour les valeurs, d'où cette formule compliqué ;)
                for j in range(4):              # enseigne de la carte
                    self.pioche.append((i, j))  # on ajoute la carte à la pioche
        self.couleur = {0 : "noir", 1 : "noir", 2 : "rouge", 3: "rouge"}
        self.enseigne = {0 : "pique", 1 : "trefle", 2 : "carreau", 3 :"coeur"}
        self.valeur = {2:"Deux", 3:"Trois", 4:"Quatre", 5:"Cinq",
                       6:"Six", 7:"Sept", 8:"Huit", 9:"Neuf", 10:"Dix",
                       11:"Valet", 12:"Dame", 13:"Roi", 14:"As", 15:"Joker"}

    def __str__(self):
        """affiche toute les cartes quand il est print"""
        return str(self.pioche)

    def nom_carte(self, t):
        "prend un tuple en paramètre et affiche la carte correspondante"
        return str(self.valeur[t[0]]+" de "+ self.enseigne[t[1]])

    def battre(self):
        """melange la pioche"""
        random.shuffle(self.pioche)

    def tirer(self):
        """retire la première carte et la return"""
        if len(self.pioche) <= 0 : return None
        return self.pioche.pop(0)

class Bataille(Jeu_de_carte):
    """
    c'est un objet qui gère le jeu de la bataille (règles dans le doc explicatif).
    4 méthodes :
    - distribuer --> distribue le jeu à 2 joueurs en parts équitables
    - jouer_instant --> le jeu pour la console
    - jouer --> le jeu pour l'interface graphique
    - verdict --> donne le vainqueur pour l'interface graphique
    """
    def __init__(self):
        super().__init__()  # récupère les attributs de Jeu_de_carte
        self.j1 =Jeu_de_carte(True)
        self.j2 =Jeu_de_carte(True)
        self.carte_gagne = {"j1":0 , "j2":0}    # dictionnaires des cartes gagnées
        self.tour = 0
        self.valeur = 2         # valeur du tour gagné, soit le nombre de carte (une bataille vaudra 6 par exemple)
        self.carte_j1 = None    # carte que le joueur vient de piocher 
        self.carte_j2 = None
    
    def distribuer(self):
        """distribue les cartes une à une entre deux joueurs"""
        self.battre()
        for _ in range(self.nombre_carte//2):   # boucle 26 fois, soit pour la moitié du paquet car on donne 2 cartes
            self.j1.pioche.append(self.tirer())
            self.j2.pioche.append(self.tirer())

    def jouer_instant(self):
        """méthode qui initialise le jeu et le gère jusqu'à la fin
         instantanément et sans interruption
         à jouer dans la console"""
        valeur = 2
        tour=0
        while tour<self.nombre_carte//2:  
        # tant que toute les cartes ne sont pas jouées
            print(f"point : j1 : {self.carte_gagne['j1']}/ j2 : {self.carte_gagne['j2']}")
            carte_j1 = self.j1.tirer()
            carte_j2 = self.j2.tirer()
            print(f"valeur de la carte du joueur 1 : {carte_j1[0]}")
            print(f"valeur de la carte du joueur 2 : {carte_j2[0]}")
            # compare les valeur des 2 cartes et attribue les point à celui qui la plus haute valeur
            if carte_j1[0] == carte_j2[0]:  
                print('BATAILLE')
                self.j1.tirer()
                self.j2.tirer()
                valeur += 4 #pour une bataille 6 (mais elle peuvent s'ajouter les unes sur les autres)
                tour+=1
            elif carte_j1[0] > carte_j2[0]:
                self.carte_gagne["j1"] += valeur
                valeur = 2
            elif carte_j1[0] < carte_j2[0]:
                self.carte_gagne["j2"] += valeur
                valeur = 2
            else:print("t bete mec, bug de la matrix XDDDDD")   # tkt frr ça se triggerera jms. sans comm
            tour+=1
        # donne le vainqueur
        print(f'j1 = {self.carte_gagne["j1"]}, j2 = {self.carte_gagne["j2"]}')
        if self.carte_gagne["j1"] > self.carte_gagne["j2"]: print("j1 a gagné")
        elif self.carte_gagne["j1"] < self.carte_gagne["j2"]: print("j2 a gagné")
        else : print("C'est une égalité")
                
    def jouer(self):
        """
        a jouer dans le tkinter
        initialise le jeu et exécute un tour
        """
        if self.tour<self.nombre_carte//2:
        # si toutes les cartes ne sont pas encore jouées
            self.carte_j1 = self.j1.tirer()
            self.carte_j2 = self.j2.tirer()
            # compare les valeur des 2 cartes et attribue les point à celui qui la plus haute valeur
            if self.carte_j1[0] == self.carte_j2[0]: 
                self.j1.tirer()
                self.j2.tirer()
                self.valeur += 4 #pour une bataille 6 (mais elle peuvent s'ajouter les unes sur les autres)
                self.tour+=1
            elif self.carte_j1[0] > self.carte_j2[0]:
                self.carte_gagne["j1"] += self.valeur
                self.valeur = 2
            elif self.carte_j1[0] < self.carte_j2[0]:
                self.carte_gagne["j2"] += self.valeur
                self.valeur = 2
            else:print("t bete mec, bug de la matrix XDDDDD")   # tkt frr ça se triggerera jms. sans comm
            self.tour+=1
        else:
            self.tour=0 # réinitialise le tour si toutes les cartes sont jouées

    def verdict(self):
        """
        utilisé pour l'interface graphique
        méthode qui donne le vainqueur :j1 --> 1 / j2 --> 2 / égalité -> 0
        """
        if self.carte_gagne["j1"] > self.carte_gagne["j2"]:
            return 1
        elif self.carte_gagne["j1"] < self.carte_gagne["j2"]:
            return 2
        elif self.carte_gagne["j1"] == self.carte_gagne["j2"]:
            return 0
        
# ------------------------------------------------------
if __name__ == "__main__":  
# se lance seulement si ce script est lancé
    bataille = Bataille()
    bataille.distribuer()
    bataille.jouer_instant()
    
    

