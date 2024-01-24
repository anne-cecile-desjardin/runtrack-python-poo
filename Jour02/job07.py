alphabet = "abcdefghijklmnopqrstuvwxyz"
chaine = ""
i=1
for i in range(1, 11):
    chaine = chaine + alphabet
while i <= len(chaine):
    print(chaine[0:i])
    i=i+2