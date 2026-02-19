# Convertisseur de poid en python

poids = float(input("Entrez le poids à convertir : "))
unit = input("Kg ou Pounds ? (K/P) : ")

if unit == "K":
    result = poids * 2.205
    print(f"{poids}Kg est égal à {result} Pounds.")
elif unit == "P":
    result = poids / 2.205
    print(f"{poids} Pounds est égal à {result}Kg.")
else:
    print(f"{unit} n'est pas un paramètre valide.")