class Livre :
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

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


livre = Livre("Le meilleur des mondes", "Huxley.A", 542)

print("Titre:", livre.get_titre())
print("Auteur:", livre.get_auteur())
print("Nombre de pages:", livre.get_pages())

livre.set_titre("Martine à la Plateforme")
livre.set_auteur("big black room")
livre.set_pages("michel")

print("\nAprès modification :")
print("Titre:", livre.get_titre())
print("Auteur:", livre.get_auteur())
print("Nombre de pages:", livre.get_pages())







        