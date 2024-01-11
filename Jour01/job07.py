class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return "Les coordonnées sont : (" + str(self.x) + ", " + str(self.y) + ")."

    def gauche(self):
        self.x -= 1
        return "Le personnage va à gauche. Coordonnées : (" + str(self.x) + ", " + str(self.y) + ")."

    def droite(self):
        self.x += 1
        return "Le personnage va à droite. Coordonnées : (" + str(self.x) + ", " + str(self.y) + ")."

    def bas(self):
        self.y -= 1
        return "Le personnage va en bas. Coordonnées : (" + str(self.x) + ", " + str(self.y) + ")."

    def haut(self):
        self.y += 1
        return "Le personnage va en haut. Coordonnées : (" + str(self.x) + ", " + str(self.y) + ")."


personnage = Personnage(3, 7)
print(personnage.position())
print(personnage.gauche())
print(personnage.droite())
print(personnage.haut())
print(personnage.bas())

