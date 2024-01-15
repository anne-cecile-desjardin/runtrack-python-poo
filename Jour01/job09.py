class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prix = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        self.prixTTC = self.prix * (1 + self.TVA / 100)
        return f"Le prix TTC est : {round(self.prixTTC,2)} €"
    
    def calculeTVA(self):
        self.TVA = self.prixTTC - self.prix
        return f"La TVA est de : {round(self.TVA,2)} €"

    def afficher(self):
        return f"Le produit {self.nom} coûte {self.prix}€ HT et {round (self.prixTTC, 2)} € TTC."

    def modifierNom(self, nom):
        self.nom = nom
        return self.nom
    
    def modifierPrixHT(self, prixHT):
        self.prix = prixHT
        return f"{round(self.prix, 2)} €"
    


p1 = Produit("banane", 1, 20)
print(p1.calculerPrixTTC())
print(p1.calculeTVA())
print(p1.afficher())
print(p1.modifierNom("pomme"))
print(p1.modifierPrixHT(2))
print(p1.calculerPrixTTC())
print(p1.calculeTVA())


p2 = Produit("orange", 1.5, 20)
print(p2.calculerPrixTTC())
print(p2.calculeTVA())
print(p2.afficher())


p3= Produit("poire", 2, 20)
print(p3.calculerPrixTTC())
print(p3.calculeTVA())
print(p3.afficher())

p4= Produit("fraise", 2.5, 20)
print(p4.calculerPrixTTC())
print(p4.calculeTVA())
print(p4.afficher())