class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie

    def get_nom(self):
        return self.__nom
    
    def get_vie(self):
        return self.__vie
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_vie(self, vie):
        self.__vie = vie

    def attaquer(self, adversaire, degats):
        adversaire.__vie -= degats
        print(f"{self.__nom} attaque {adversaire.__nom} et lui inflige {degats} points de dégâts.")



class Jeu:
    def __init__(self):
        self.__niveau = 0

    def get_niveau(self):
        return self.__niveau
    
    def set_niveau(self, niveau):
        self.__niveau = niveau

    def choisirNiveau(self):
        self.__niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 moyen, 3 difficile): "))

    def lancerJeu(self):
        self.choisirNiveau()

        if self.__niveau == 1:
            vie_joueur = 100
            vie_ennemi = 80
        elif self.__niveau == 2:
            vie_joueur = 80
            vie_ennemi = 100
        elif self.__niveau == 3:
            vie_joueur = 70
            vie_ennemi = 120
        else:
            print("Niveau invalide. Le jeu se termine.")
            return

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        self.deroulementPartie(joueur, ennemi)

    def verifierSante(self, personnage):
        if personnage.get_vie() <= 0:
            print(f"{personnage.get_nom()} n'a plus de vie.")
            return True
        return False

    def determinerGagnant(self, joueur, ennemi):
        if joueur.get_vie() > ennemi.get_vie():
            print("Le joueur a gagné!")
        elif joueur.get_vie() < ennemi.get_vie():
            print("L'ennemi a gagné!")
        else:
            print("Match nul!")

    def deroulementPartie(self, joueur, ennemi):
        while True:
            joueur.attaquer(ennemi, 20)

            if self.verifierSante(ennemi):
                print("La partie est terminée.")
                self.determinerGagnant(joueur, ennemi)
                break

            ennemi.attaquer(joueur, 15)

            if self.verifierSante(joueur):
                print("La partie est terminée.")
                self.determinerGagnant(joueur, ennemi)
                break

jeu = Jeu()
jeu.lancerJeu()
