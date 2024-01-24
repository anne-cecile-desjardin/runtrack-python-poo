class Joueur:
    def __init__(self, nom, numero, position, nb_but_marques, passe_decisive, carton_jaune, carton_rouge) :
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__nb_but_marques = nb_but_marques
        self.__passe_decisive = passe_decisive
        self.__carton_jaune = carton_jaune
        self.__carton_rouge = carton_rouge

    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom


    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero):
        self.__numero = numero

    def get_position(self):
        return self.__position
    
    def set_position(self, position):
        self.__position = position
    
    def get_nb_but_marques(self):
        return self.__nb_but_marques
    
    def set_nb_but_marques(self, nb_but_marques):
        self.__nb_but_marques = nb_but_marques

    def get_passe_decisive(self):
        return self.__passe_decisive
    
    def set_passe_decisive(self, passe_decisive):
        self.__passe_decisive = passe_decisive

    def get_carton_jaune(self):
        return self.__carton_jaune
    
    def set_carton_jaune(self, carton_jaune):
        self.__carton_jaune = carton_jaune

    def get_carton_rouge(self):
        return self.__carton_rouge
    
    def set_carton_rouge(self, carton_rouge):
        self.__carton_rouge = carton_rouge

    def marquer_un_but(self):
        self.__nb_but_marques += 1
    
    def effectuer_une_passe_decisive(self):
        self.__passe_decisive += 1
    
    def recevoir_un_carton_jaune(self):
        self.__carton_jaune += 1

    def recevoir_un_carton_rouge(self):
        self.__carton_rouge += 1

    def afficher_statistiques(self):
        print("Nom : ", self.__nom)
        print("Numero : ", self.__numero)
        print("Position : ", self.__position)
        print("Nombre de buts marqués : ", self.__nb_but_marques)
        print("Nombre de passes décisives : ", self.__passe_decisive)
        print("Nombre de cartons jaunes : ", self.__carton_jaune)
        print("Nombre de cartons rouges : ", self.__carton_rouge)


    
class Equipe:
    def __init__(self, nom) :
        self.__nom = nom
        self.__list_joueur = []

    def ajouter_joueur(self, joueur):
        self.__list_joueur.append(joueur)


    # Faire afficher statistiques d'un seul joueur
    # def afficher_statistiques_joueurs(self, num_joueur):
    #     for joueur in self.__list_joueur:
    #         if joueur.get_numero() == num_joueur:
    #             joueur.afficher_statistiques()
    #             break


    def afficher_statistiques_joueurs(self, joueur):
        for joueur in self.__list_joueur:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueur(self, num_joueur, nb_but_marques, passe_decisive, carton_jaune, carton_rouge):
        for joueur in self.__list_joueur:
            if joueur.get_numero() == num_joueur:
                joueur.set_nb_but_marques(nb_but_marques)
                joueur.set_passe_decisive(passe_decisive)
                joueur.set_carton_jaune(carton_jaune)
                joueur.set_carton_rouge(carton_rouge)


equipe1 = Equipe("Equipe1")
equipe2 = Equipe("Equipe2")

joueur1 = Joueur("Joueur1", 1, "Attaquant", 0, 0, 0, 0)
joueur2 = Joueur("Joueur2", 2, "Attaquant", 0, 0, 0, 0)
joueur3 = Joueur("Joueur3", 3, "Attaquant", 0, 0, 0, 0)
joueur4 = Joueur("Joueur4", 4, "Attaquant", 0, 0, 0, 0)
joueur5 = Joueur("Joueur5", 5, "Gardien", 0, 0, 0, 0)
joueur6 = Joueur("Joueur6", 6, "Milieu", 0, 0, 0, 0)
joueur7 = Joueur("Joueur7", 7, "Milieu", 0, 0, 0, 0)
joueur8 = Joueur("Joueur8", 8, "Défenseur", 0, 0, 0, 0)
joueur9 = Joueur("Joueur9", 9, "Défenseur", 0, 0, 0, 0)
joueur10 = Joueur("Joueur10", 10, "Défenseur", 0, 0, 0, 0)
joueur11 = Joueur("Joueur11", 11, "Défenseur", 0, 0, 0, 0)

joueur12 = Joueur("Joueur12", 12, "Attaquant", 0, 0, 0, 0)
joueur13 = Joueur("Joueur13", 13, "Attaquant", 0, 0, 0, 0)
joueur14 = Joueur("Joueur14", 14, "Attaquant", 0, 0, 0, 0)
joueur15 = Joueur("Joueur15", 15, "Attaquant", 0, 0, 0, 0)
joueur16 = Joueur("Joueur16", 16, "Gardien", 0, 0, 0, 0)
joueur17 = Joueur("Joueur17", 17, "Milieu", 0, 0, 0, 0)
joueur18 = Joueur("Joueur18", 18, "Milieu", 0, 0, 0, 0)
joueur19 = Joueur("Joueur19", 19, "Défenseur", 0, 0, 0, 0)
joueur20 = Joueur("Joueur20", 20, "Défenseur", 0, 0, 0, 0)
joueur21 = Joueur("Joueur21", 21, "Défenseur", 0, 0, 0, 0)
joueur22 = Joueur("Joueur22", 22, "Défenseur", 0, 0, 0, 0)

equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur2)
equipe1.ajouter_joueur(joueur3)
equipe1.ajouter_joueur(joueur4)
equipe1.ajouter_joueur(joueur5)
equipe1.ajouter_joueur(joueur6)
equipe1.ajouter_joueur(joueur7)
equipe1.ajouter_joueur(joueur8)
equipe1.ajouter_joueur(joueur9)
equipe1.ajouter_joueur(joueur10)
equipe1.ajouter_joueur(joueur11)

equipe2.ajouter_joueur(joueur12)
equipe2.ajouter_joueur(joueur13)
equipe2.ajouter_joueur(joueur14)
equipe2.ajouter_joueur(joueur15)
equipe2.ajouter_joueur(joueur16)
equipe2.ajouter_joueur(joueur17)
equipe2.ajouter_joueur(joueur18)
equipe2.ajouter_joueur(joueur19)
equipe2.ajouter_joueur(joueur20)
equipe2.ajouter_joueur(joueur21)
equipe2.ajouter_joueur(joueur22)



equipe1.afficher_statistiques_joueurs(joueur6)

joueur1.marquer_un_but()
joueur3.marquer_un_but()
joueur8.recevoir_un_carton_jaune()
joueur20.recevoir_un_carton_jaune()
joueur8.recevoir_un_carton_rouge()
joueur16.marquer_un_but()

equipe1.afficher_statistiques_joueurs(joueur1)

