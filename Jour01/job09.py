class Produit:

    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        
        prixTTC = self.prixHT * (1 + self.TVA)

        return "Le prix du produit TTC est : " + str(prixTTC) + " euro(s)"
    
    def afficher(self):
        return "Les informations du produit sont : Nom : " + str(self.nom) + "; PrixHT : " + str(self.prixHT) + " euro(s)" + "; TVA appliquée : " + str(self.TVA) + "."
    
    def nomProduit(self):
        return str(self.nom)
    
    def prixProduit(self):
        return str(self.prixHT)

produit1 = Produit("Pâtisson", 3, 0.2)
produit2 = Produit("Pastèque", 5, 0.2)
produit3 = Produit("Téléphone", 350, 0.2)
produit4 = Produit("Voiture", 5000, 0.2)

print(produit1.afficher(), produit1.CalculerPrixTTC(), produit2.afficher(), produit2.CalculerPrixTTC(), produit3.afficher(), produit3.CalculerPrixTTC(), produit4.afficher(), produit4.CalculerPrixTTC())
