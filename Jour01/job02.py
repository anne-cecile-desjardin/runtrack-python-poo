class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

p = Operation(1, 2)

print("Le nombre 1 est", p.nombre1)
print("Le nombre 2 est", p.nombre2)