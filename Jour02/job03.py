class Livre:
    def __init__(self, titre, auteur, pages, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = disponible

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_pages(self):
        return self.__pages
                
    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif!")

    def get_disponible(self):
        return self.__disponible
    
    def set_disponible(self, disponible):
        self.__disponible = disponible 

    def verification(self):
        return self.__disponible
        
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Livre emprunté")
        else: 
            print("Le livre n'est pas disponible")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Livre rendu")
        else:
            print("Le livre n'a pas été emprunté.")


livre = Livre("Toto et tutu", "Titi", 200, True)

print("Vérification de la disponibilité :", livre.verification())

livre.emprunter()
print("Vérification après emprunt :", livre.verification())

livre.rendre()
print("Vérification après rendu :", livre.verification())

        