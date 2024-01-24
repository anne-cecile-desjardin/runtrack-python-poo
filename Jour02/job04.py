N = int(input("Entez un entier supperieur à zéro: "))
for i in range(1, N+1):
    print(f"Table de multiplication de {i}")
    for j in range(1, 10+1):
        print(f"{i} x {j} = {i*j}")
    print("\n")