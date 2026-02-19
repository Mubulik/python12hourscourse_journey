# Panier de course

bouffes = []
prix = []
total = 0

while True:
    bouffe = input("Entrez le nom de la nourriture à acheter (q pour quitter) : ")
    if bouffe.lower() == "q":
        break
    else:
        tarif = float(input(f"Entrez le prix de {bouffe} (€) : "))
        bouffes.append(bouffe)
        prix.append(tarif)

print("------- Votre Panier -------")

for bouffe in bouffes:
    print(bouffe, end=" ; ")

for tarif in prix:
    total += tarif
print(f"\nTotal du panier = {total:02}€")