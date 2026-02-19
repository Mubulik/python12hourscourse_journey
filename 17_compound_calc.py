# Calculateur d'intérêts composés en python

capital = 0
coef = 0
temps = 0


while capital <= 0:
    capital = float(input("Entrez votre capital d'investissement de départ : "))
    if capital <= 0:
        print("Le capital de départ ne peut pas être inférieur ou égal à 0.")

while True:
    coef = float(input("Indiquez le taux visé : "))
    if coef < 0:
        print("Le taux ne peut pas être inférieur à 0.")
    else:
        break

while temps <= 0:
    temps = float(input("Indiquez le nombre d'années d'épargne : "))
    if temps <= 0:
        print("Le nombre d'années ne peut pas être inférieur ou égal à 0.")

if (input(f"Vous avez, \nUn capital départ de {capital}€\nUn taux de {coef}%\nPour {temps} ans. \nContinuer ? (O/N) : ")) == "O":
    total = capital * pow((1 + coef / 100),temps)
    print(f"Voici votre résultat final à partir des informations fournies :\n{total:5}€")
else:
    exit