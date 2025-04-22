Travail effectué par Jean Salomon, Isidore Billard, Baptiste Bumann

Dossier:
    -README.txt
    le document explicatif

    -main.py
    le code principal contenant tout ce qui gère le jeu

    -graphic_interface.py
    un code utilisant la librairie "Tkinter" pour avoir une interface graphique 
    pour le jeu de la bataille

    -img
    contient toutes les images utilisés pour l'interface graphique

1.  Classes et fonctions (méthodes):
    main.py:  
        On a créé une classe nommé Jeu_de_carte qui contient toutes les cartes, on peut soit:
        l’instancier vide (jeux des deux joueurs qui s’affrontent)
        l’instancier avec 52 cartes (jeu de carte de base qu’on trie et distribue)
        Les attributs de Jeu_de_carte sont:
            nombre_carte => le nombre de cartes que ce tas contiendra
            pioche => toutes les cartes sous forme de liste de tuples (valeur, enseigne)
            couleur => dictionnaire des couleurs par rapport aux enseignes
            enseigne => dictionnaire des enseignes des cartes (Pique, trèfle, carreaux ,cœur)
            valeur => dictionnaire des valeurs que peuvent prendre les cartes (1 à 10, Valet, Dame, Roi, As)
        Et ses paramètres:
            empty => booléen qui gère si le jeu est vide ou rempli lors de sa création
            nb_cartes => le nombre de carte qu’il y aura dans le jeu
        Et ses méthodes:
            nom_carte => renvoie sous forme de str le nom de la carte(à partir des dictionnaires)
            battre => mélange le jeu (pioche) de façon aléatoire
            tirer => retire et renvoie la première carte du paquet
        Dans le constructeur, on a la mise en place de toutes les cartes dans l’attribut pioche grâce à des boucles “for”
        et la mise en place des dictionnaires qui vont servir d’index pour les cartes (valeur et enseigne).

        Ensuite, on a créé une deuxième classe "Bataille" qui hérite de la classe "Jeu_de_carte", qui contient
        un jeu de cartes avec toutes les méthodes nécessaires pour y jouer.
        Les attributs de Bataille sont:
            j1 => joueur 1 avec son paquet de cartes vide
            j2 => joueur 2 avec don paquet de cartes vide
            carte_gagne => dictionnaire contenant les points de joueurs
            tour => nombre de tour effectué pour “jouer” avec le tkinter
        Et ses méthodes:
            distribuer => distribue les cartes de manière aléatoire entre les 2 joueurs
            jouer_instant => joue le jeu dans la console de manière instantanée
            jouer => joue le jeu dans le tkinter avec des interactions avec le joueur
            verdict => méthode qui décide de quel joueur gagne le tour en comparant le nombre de cartes gagnés et renvoyant un nombre 
            qui correspond à un certain cas, 0 => égalité, 1 => joueur 1 gagne, 2 => joueur 2 gagne
        Dans le constructeur, on a la mise en place des 2 paquets de cartes pour les 2 joueurs, suivi par les points des joueurs et le nombre de tour écoulé.
    graphic_interface.py :
        On réutilise le code de la classe Bataille pour créer le même jeu avec une interface graphique.
        On a 2 fonction dans ce code:
            charger_image => fonction qui sert sert à charger les images. Elle prend en parametre : le chemin d'acces(chemin),
                            indice du debut(index_debut) et fin/le nombre d'image(nb_image), un tuple pour la taille de l'image 
                            et booléen pour savoir si l'image doit être tournée ou non
                            on utilisera la methode ".extend" pour remplir une liste si besoin
            turn => fonction qui controle le fonctionnement du tour avec les comparaisons de cartes, lancée par le button "tour"
2.  Comparaison de la valeur des cartes:
    On a trois possibilités pour les comparaisons des cartes, qui se fait à partir de la valeur des cartes qu’on tire (ex: 3 (trois) < 14 (As)):
    carte 1 = carte 2, les 2 cartes sont égales donc on a une bataille: on garde de côté les 2 cartes tirées et on en tire 2 autres, 
        la prochaine comparaison ne donnera plus 2 points (car on mettait en jeu 2 cartes), mais 6, soit +4, c’est la variable valeur qui est modifiée, 
        et une autre comparaison est lancé (avec 6 points en jeu car on a posé 6 cartes, plus 4 si on a déjà une bataille), 
        après cette dernière tout revient à la normale avec valeur = 2.
        La seule exception est si une bataille se produit à la fin, alors on ajoute pas de points (plus assez de cartes)

    carte 1 < carte 2, le joueur 2 gagne cette comparaison et donc 2 points (2 cartes) ou le nombre de carte posé si il y a eu une bataille
    carte 1 > carte 2, le joueur 1 gagne cette comparaison et donc 2 points (2 cartes) ou le nombre de carte posé si il y a eu une bataille


3. Jeu de test : 
    Comme jeu de test voici le déroulement d’une partie instantanée 
    avec la valeur des cartes et le nombre de point de chaque joueurs :

    point : j1 : 0/ j2 : 0
    valeur de la carte du joueur 1 : 12
    valeur de la carte du joueur 2 : 12
    BATAILLLLLE!!!!!!!
    point : j1 : 0/ j2 : 0
    valeur de la carte du joueur 1 : 12
    valeur de la carte du joueur 2 : 10
    point : j1 : 6/ j2 : 0
    valeur de la carte du joueur 1 : 2
    valeur de la carte du joueur 2 : 6
    point : j1 : 6/ j2 : 2
    valeur de la carte du joueur 1 : 14
    valeur de la carte du joueur 2 : 5
    point : j1 : 8/ j2 : 2
    valeur de la carte du joueur 1 : 11
    valeur de la carte du joueur 2 : 4
    point : j1 : 10/ j2 : 2
    valeur de la carte du joueur 1 : 7
    valeur de la carte du joueur 2 : 6
    point : j1 : 12/ j2 : 2
    valeur de la carte du joueur 1 : 10
    valeur de la carte du joueur 2 : 11
    point : j1 : 12/ j2 : 4
    valeur de la carte du joueur 1 : 14
    valeur de la carte du joueur 2 : 8
    point : j1 : 14/ j2 : 4
    valeur de la carte du joueur 1 : 5
    valeur de la carte du joueur 2 : 3
    point : j1 : 16/ j2 : 4
    valeur de la carte du joueur 1 : 10
    valeur de la carte du joueur 2 : 9
    point : j1 : 18/ j2 : 4
    valeur de la carte du joueur 1 : 6
    valeur de la carte du joueur 2 : 5
    point : j1 : 20/ j2 : 4
    valeur de la carte du joueur 1 : 13
    valeur de la carte du joueur 2 : 4
    point : j1 : 22/ j2 : 4
    valeur de la carte du joueur 1 : 14
    valeur de la carte du joueur 2 : 14
    BATAILLLLLE!!!!!!!
    point : j1 : 22/ j2 : 4
    valeur de la carte du joueur 1 : 2
    valeur de la carte du joueur 2 : 2
    BATAILLLLLE!!!!!!!
    point : j1 : 22/ j2 : 4
    valeur de la carte du joueur 1 : 7
    valeur de la carte du joueur 2 : 3
    point : j1 : 32/ j2 : 4
    valeur de la carte du joueur 1 : 4
    valeur de la carte du joueur 2 : 11
    point : j1 : 32/ j2 : 6
    valeur de la carte du joueur 1 : 9
    valeur de la carte du joueur 2 : 12
    point : j1 : 32/ j2 : 8
    valeur de la carte du joueur 1 : 8
    valeur de la carte du joueur 2 : 8
    BATAILLLLLE!!!!!!!
    point : j1 : 32/ j2 : 8
    valeur de la carte du joueur 1 : 2
    valeur de la carte du joueur 2 : 13
    point : j1 : 32/ j2 : 14
    valeur de la carte du joueur 1 : 7
    valeur de la carte du joueur 2 : 9
    point : j1 : 32/ j2 : 16
    valeur de la carte du joueur 1 : 8
    valeur de la carte du joueur 2 : 4
    point : j1 : 34/ j2 : 16
    valeur de la carte du joueur 1 : 6
    valeur de la carte du joueur 2 : 10
    j1 = 34, j2 = 18
    j1 a gagné

