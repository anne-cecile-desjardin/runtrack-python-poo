class Tache:

    def __init__(self, titre, description, statut = "à faire"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
        
    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

    def get_statut(self):
        return self.__statut
    
    def set_statut(self, statut):
        self.__statut = statut


class ListeDeTaches:
        
    def __init__(self):
        self.__taches = []  

    def ajouterTache(self, tache):
        self.__taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.__taches:
            if tache.get_titre() == titre:  
                self.__taches.remove(tache)

    def marquerCommeFinie(self, titre):
        for tache in self.__taches:
            if tache.get_titre() == titre:  
                tache.set_statut("terminée")  

    def afficherListe(self):
        return [(tache.get_titre(), tache.get_description(), tache.get_statut()) for tache in self.__taches]

    def filterListe(self, statut):
        return [(tache.get_titre(), tache.get_description(), tache.get_statut()) for tache in self.__taches if tache.get_statut() == statut]



tache1 = Tache("Faire les courses", "Acheter des fruits et des bouillons cube")
tache2 = Tache("Finir carrelage", "Acheter les carrelage pour la cuisine")
tache3 = Tache("Boire de l'eau", "toutes les heures")

liste_taches = ListeDeTaches()


liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)


print("Liste avant modification:")
print(liste_taches.afficherListe())

liste_taches.supprimerTache("Faire les courses")
liste_taches.ajouterTache(tache3)


liste_taches.marquerCommeFinie("Finir carrelage")


print("\nListe après modification:")
print(liste_taches.afficherListe())

taches_a_faire = liste_taches.filterListe("à faire")
print("\nTâches à faire:")
print(taches_a_faire)