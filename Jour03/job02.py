
class CompteBancaire:

    def __init__(self, num_compte, nom, prenom, solde, decouvert = True):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def get_num_compte(self):
        return self.__num_compte
    
    def set_num_compte(self, num_compte):
        self.__num_compte = num_compte

    def get_prenom(self):
        return self.__prenom
    
    def set_prenom(self, prenom):
        self.__prenom = prenom

    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom

    def get_solde(self):
        return self.__solde
    
    def set_solde(self, solde):
        self.__solde = solde

    def get_decouvert(self):
        return self.__decouvert
    
    def set_decouvert(self, decouvert):
        self.__decouvert = decouvert

   
    def afficher_detail(self):
        print(f"\nNuméro de compte: {self.__num_compte}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Solde: {self.__solde} €\n")

    def afficher_solde(self):
        print (f"Le solde du compte{self.get_num_compte()} est {self.get_solde()}")

    def versement(self, montant_verse):
        self.__solde += montant_verse
        print(f"Montant de {montant_verse} € à été versé sur votre compte")

    def retrait(self, montant_retire):
        if self.__solde < montant_retire and self.__decouvert == False:
            print("Solde du compte insuffisant")
        else: 
            self.__solde -= montant_retire
            self.decouvert()
            print(f"Montant de {montant_retire} € à été retiré de votre compte")

    def decouvert(self, taux_agios = 0.5):
        if self.__decouvert == True and self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Des agios de {agios} € ont été appliqués. Nouveau solde: {self.__solde} €")

    def virement(self,reference, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.get_num_compte()}.")
        else:
            print("Solde insuffisant. Virement annulé.")
        

compte1 = CompteBancaire(1, "Vanni", "Barbara", 1750)

compte2 = CompteBancaire(2, "Toto", "Fifi", -20)

compte1.afficher_detail()

compte1.versement(50)
compte1.afficher_solde()

compte1.retrait(1000)
compte1.afficher_solde()

compte2.afficher_detail()

compte1.virement(1,compte2, 20)
compte1.afficher_solde()

compte2.afficher_solde()



