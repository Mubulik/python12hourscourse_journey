# Théorème de pythagore
import math


a = float(input("Entrez la taille du côté A : "))
b = float(input("Entez la taille du côté B : "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"D'après le théorème de Pythagore, l'hypoténuse C du triangle ABC, avec A = {a} et B = {b}, est égale à {c}.")