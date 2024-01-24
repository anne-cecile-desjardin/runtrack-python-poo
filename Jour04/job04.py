class Form:
    def __init__(self):
        pass
    def aire(self):
        return 0


class Rectangle(Form):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def aire(self):
        return self.length * self.width
    

rectangle = Rectangle(5, 10)
print(rectangle.aire())