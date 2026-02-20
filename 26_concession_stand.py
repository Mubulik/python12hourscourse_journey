# Concession stand program

menu = {"Small Popcorn":1.50,
        "Media Popcorn":2.50,
        "Large Popcorn":3.00,
        "M&Ms":2.99,
        "Candies":2.49,
        "Soda":1.99}

panier = []
total = 0

for item, price in menu.items():
    print("-----------------------")
    print(f"{item} - {price:.2f}€")
print("-----------------------")

while True:
    pending = input("Que souhaitez vous achetez? (q pour quitter): ")
    print()
    if pending in menu.keys():
        panier.append(pending)
        total += menu[pending]
        print(f"Votre panier contient les articles suivants : {panier} pour un total de {total:.2f}€.\n")
    elif pending == "q":
        break
    else:
        print("Cet article n'existe pas. Veuillez choisir un item dans le menu.\n")

print("\nVoici votre panier :")
for item in panier:
    print(f"{item} - {menu[item]}€")

print(f"Pour un total de : {total}€")
print("\nMerci et bonne journée :D")