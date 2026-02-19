# nested loop = une loop dans une autre loop (outer, inner // externe, interne)
#               outer loop:
#                   inner loop:

lignes = int(input("Entrez le nombre de lignes : "))
colones = int(input("Entrez le nombre de colones : "))
symbole = input("Entrez le symbole séparateur : ")

for x in range(lignes):
    for i in range(colones):
        print(symbole, end="")
    print()