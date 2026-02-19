# Convertisseur de température en python

temp = float(input("Entrez la température à convertir : "))
unit = input("Quelle est l'unité de température initiale, Celius/Fahrenheit? (C/F) : ")

if unit == "C":
    result = temp*1.8 + 32
    print(f"{temp}°C est égal à {result}°F.")
elif unit == "F":
    result = (temp - 32) / 1.8
    print(f"{temp}°F est égal à {result}°C.")
else:
    print(f"{unit} n'est pas un paramètre valide.")