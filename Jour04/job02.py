class Personnage:
    def __init__(self, age = 14):
        self._age = age

    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age

    def afficherAge(self):
        print(f"Le personnage a {self._age} ans.")

    def bonjour(self):
        print("Bonjour.")

    def modifierAge(self, age):
        self.age = int(age)


class Eleve(Personnage):
    def __init__(self, age):
        Personnage.__init__(self,age)

    def allerEnCours(self):
        print("Je vais en cours.")

    def afficherAge(self):
        print(f"J'ai {self._age} ans.")

class Professeur(Personnage):
    def __init__(self, age, matiereEnseignee):
        Personnage.__init__(self, age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print(f"Le cours {self.__matiereEnseignee} va commencer")


eleve = Eleve(14)
gardien = Personnage(50)
professeur = Professeur(40, "Python")

eleve.afficherAge()
eleve.bonjour()
eleve.allerEnCours()
eleve.set_age(15)
eleve.afficherAge()

professeur.bonjour()
professeur.enseigner()
