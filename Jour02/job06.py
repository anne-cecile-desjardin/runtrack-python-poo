class Commande:
    def __init__(self, num_commande, statut_commande = "en cours"):
        self.__num_commande = num_commande
        self.__plat_commande = {}
        self.__statut_commande = statut_commande


    def get_num_commande(self):
        return self.__num_commande
    
    def set_num_commande(self, num_commande):
        self.__num_commande = num_commande

    def get_plat_commande(self):
        return self.__plat_commande
    
    def set_plat_commande(self, plat_commande):
        self.__plat_commande = plat_commande

    def get_statut_commande(self):
        return self.__statut_commande
    
    def set_statut_commande(self, statut_commande):
        self.__statut_commande = statut_commande
    


    def ajout_plat(self, nom_plat, prix_plat):
        if nom_plat in self.__plat_commande:
            print(f"{nom_plat} est déjà en commande")
        else :
            self._Commande__plat_commande[nom_plat] = {'prix': prix_plat, 'statut': 'En cours'}

    def annuler_plat(self, nom_plat):
        if nom_plat in self.__plat_commande:
            del self.__plat_commande[nom_plat]
            print(f"Plat '{nom_plat}' annulé de la commande.")
        else:
            print(f"Le plat '{nom_plat}' n'est pas dans la commande.")
        return self.__plat_commande

    def __total_payer(self):
        total = sum(plat['prix'] for plat in self.__plat_commande.values())
        return total

    def afficher_commande(self):
        print(f"\nCommande n°{self.__num_commande}:")
        for plat, details in self.__plat_commande.items():
            print(f"{plat} - {details['prix']} € ({details['statut']})")
        total = self.__total_payer()
        print(f"\nTotal à payer: {total} € (TVA incluse)")

    def calcul_TVA(self, taux_tva):
        total = self.__total_payer()
        tva = total * (taux_tva / 100)
        print(f"TVA ({taux_tva}%): {tva} €")


commande1 = Commande(1)

commande1.ajout_plat ("Poulet curry", 13)
commande1.ajout_plat ("Tatami de dojo", 9.50)
commande1.ajout_plat ("Rognure d'ongle", 10)

commande1.calcul_TVA(20)

commande1.afficher_commande()

commande1.annuler_plat("Poulet curry")
commande1.afficher_commande()



    