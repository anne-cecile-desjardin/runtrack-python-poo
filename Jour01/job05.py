class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return "Les coordonnées de x sont : " + str(self.x) + ". Les coordonnées de y sont : " + str(self.y) + "."

    def afficherX(self):
        print("La valeur de x est : ", self.x, ".")

    def afficherY(self):
        print("La valeur de y est : ", self.y, ".")

    def changerX(self, new_x):
        self.x = new_x
        print("La valeur de x est changée par : ", self.x, ".")

    def changerY(self, new_y):
        self.y = new_y
        print("La valeur de y est changée par : ", self.y, ".")


point = Point(3, 7)
print(point.afficherLesPoints())
point.afficherX()
point.afficherY()
point.changerX(5)
point.changerY(10)
