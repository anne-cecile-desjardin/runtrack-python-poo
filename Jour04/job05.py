from math import pi

class Form:
    def __init__(self):
        pass
    def aire(self):
        return 0
    
class Cercle(Form):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return (pi) * self.radius ** 2
    
class Rectangle(Form):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def aire(self):
        return self.length * self.width
    

rectangle = Rectangle(5, 10)
print(rectangle.aire())
    
cercle = Cercle(6)
print(cercle.aire())