# Shopping cart program

item = input("Quel article souhaitez-vous ajouter au panier? : ")
prix = float(input("Quel est le prix de ce dernier? : "))
quantity = int(input("Combien de ce dernier souhaitez-vous acheter? : "))

prix_total = prix * quantity

print(f"Le panier contient {quantity} {item}, pour un coût total de {prix_total}€.")