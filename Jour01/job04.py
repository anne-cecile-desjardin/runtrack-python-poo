class Personne:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
    
    def SePresenter(self):
        return "Je suis " + self.surname + " " + self.name


p1 = Personne("John", "Doe")
p2 = Personne("Jean", "Dupont")

result1 = p1.SePresenter()
result2 = p2.SePresenter()


print(result1)
print(result2)