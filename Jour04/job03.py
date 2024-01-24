class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length
    def set_length(self, length):
        self.length = length
    
    def get_width(self):
        return self.width
    def set_width(self, width):
        self.width = width

    def surface(self):
        return self.length * self.width

    def perimetre(self):
        return 2 * (self.length + self.width)
    
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def get_height(self):
        return self.height
    def set_height(self, height):
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


rectangle = Rectangle(5, 10)
parallelepipede = Parallelepipede(5, 10, 15)

print(f"Surface du rectangle: {rectangle.surface()}")
print(f"Perimetre du rectangle: {rectangle.perimetre()}")
print(f"Volume du parallelepipede: {parallelepipede.volume()}")
