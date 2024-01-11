class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def vieillir(self):
        self.age += 1
        return "L'age de l'animal est " + str(self.age) + "."

    def nommer(self):
        return "L'animal se nomme " + self.name

p1 = Animal(0, "Luna")

result1 = p1.vieillir() + " " + p1.nommer()


print(result1)



