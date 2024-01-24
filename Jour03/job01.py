class Ville:
    def __init__(self, nom_ville, nb_habitant):
        self.__nom_ville = nom_ville
        self.__nb_habitant = nb_habitant
    
    def get_nom_ville(self):
        return self.__nom_ville
    
    def set_nom_ville(self, nom_ville):
        self.__nom_ville = nom_ville

    def get_nb_habitant(self):
        return self.__nb_habitant
    
    def set_nb_habitant(self, nb_habitant):
        self.__nb_habitant = nb_habitant


class Personne:
    def __init__(self, nom_habitant, age, ville):
        self.__nom_habitant = nom_habitant
        self.__age = age
        self.__ville = ville

    def get_nom_ville(self):
        return self.__ville.get_nom_ville()

    def set_nom_ville(self, nom_ville):
        self.__ville.set_nom_ville(nom_ville)

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def get_nom_habitant(self):
        return self.__nom_habitant
    
    def set_nom_habitant(self, nom_habitant):
        self.__nom_habitant = nom_habitant

    def ajouter_population(self):
        self.__ville.set_nb_habitant(self.__ville.get_nb_habitant() + 1)


Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)
print(f"Population de la ville de Paris : {Paris.get_nb_habitant()}")
print(f"Population de la ville de Marseille : {Marseille.get_nb_habitant()}")

John = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Chloe = Personne("Chloé", 18, Marseille)

John.ajouter_population()
Myrtille.ajouter_population()
Chloe.ajouter_population()


print(f"Mise à jour du nombre d'habitants de la ville de {Paris.get_nom_ville()}: {Paris.get_nb_habitant()}")
print(f"Mise à jour du nombre d'habitants de la ville de {Marseille.get_nom_ville()}: {Marseille.get_nb_habitant()}")



