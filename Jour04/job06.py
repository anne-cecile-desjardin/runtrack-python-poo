class Vehicule:
    def __init__(self,marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def get_marque(self):
        return self.marque
    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele
    def set_modele(self, modele):
        self.modele = modele

    def get_annee(self):
        return self.annee
    def set_annee(self, annee):
        self.annee = annee

    def get_prix(self):
        return self.prix
    def set_prix(self, prix):
        self.prix = prix

    def informationVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modele: {self.modele}")
        print(f"Annee: {self.annee}")
        print(f"Prix: {self.prix}")

    def demarrer(self):
        print(f"\nAttention, je roule")
    

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, nbPortes = 4):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.nbPortes = nbPortes

    def get_nbPortes(self):
        return self.nbPortes
    def set_nbPortes(self, nbPortes):
        self.nbPortes = nbPortes

    def informationVehicule(self):
        print(f"\nMarque: {self.marque}")
        print(f"Modele: {self.modele}")
        print(f"Annee: {self.annee}")
        print(f"Prix: {self.prix}")
        print(f"Nombre de portes: {self.nbPortes}")
    
    def demarrer(self):
        print(f"\nVroooooum vroum !!!")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, nbRoues = 2):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.nbRoues = nbRoues

    def get_nbRoues(self):
        return self.nbRoues
    def set_nbRoues(self, nbRoues):
        self.nbRoues = nbRoues

    def informationVehicule(self):
        print(f"\nMarque: {self.marque}")
        print(f"Modele: {self.modele}")
        print(f"Annee: {self.annee}")
        print(f"Prix: {self.prix}")
        print(f"Nombres de roues: {self.nbRoues}")

    def demarrer(self):
        print(f"\nAttention au pot, il est chaud ")

opel = Voiture("Opel", "Corsa", 2010, 5000, 5)
suzuki = Moto("Suzuki", "GSX-R", 2015, 10000)
opel.informationVehicule()
suzuki.informationVehicule()
opel.demarrer()
suzuki.demarrer()