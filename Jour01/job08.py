class Cercle:

    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def afficherInfos(self):
        return "Les informations des cercles sont : " + str(self.r1) + ", " + str(self.r2) + "."

    def changerRayon(self):
        self.r1 += 2
        self.r2 += 5
        return "Le rayon des cercles ont changé. Informations : " + str(self.r1) + ", " + str(self.r2) + "."

    def circonference(self):
        circonference1 = 2 * self.r1 * 3.14
        circonference2 = 2 * self.r2 * 3.14
        return "Les circonférences des cercles sont : " + str(circonference1) + ", " + str(circonference2) + "."

    def aire(self):
        aire1 = 3.14 * self.r1**2
        aire2 = 3.14 * self.r2**2
        return "Les aires des cercles sont : " + str(aire1) + ", " + str(aire2) + "."

    def diametre(self):
        diametre1 = 2 * self.r1
        diametre2 = 2 * self.r2
        return "Les diamètres des cercles sont : " + str(diametre1) + ", " + str(diametre2) + "."

cercle = Cercle(3, 7)

print(cercle.afficherInfos())
print(cercle.changerRayon())
print(cercle.circonference())
print(cercle.aire())
print(cercle.diametre())
