class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def en_marche(self):
        return self.__en_marche

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele
    
    def set_annee(self, annee):
        self.__annee = annee
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Pas assez d'essence !!!!")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

    def __verifier_plein(self):
        return self.__reservoir > 5


ma_voiture = Voiture("Opel", "Adam", 2013, 10000, 4)

# print("Marque :", ma_voiture.get_marque())
# print("Modèle :", ma_voiture.get_modele())
# print("Année :", ma_voiture.get_annee())
# print("Kilométrage :", ma_voiture.get_kilometrage())
# print("En marche :", ma_voiture.en_marche())

ma_voiture.demarrer()
print("En marche après démarrage :", ma_voiture.en_marche())


ma_voiture.arreter()
print("En marche après arrêt :", ma_voiture.en_marche())


