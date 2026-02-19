# while loop = execute du code TANT QUE quelconque condition est vérifiée

name = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))

while name == "":
    print("Vous n'avez pas renseigné votre nom.")
    name = input("Entrez votre nom : ")

while not 99 > age > 0:
    print("Votre âge doit être compris en 0 et 99 ans.")
    age = int(input("Entrez votre âge : "))

print(f"Salut {name} ! \nTu as {age} ans :D")


food = input("Entrez votre plat favori (q pour quitter) : ")

while not food=="q":
    print(f"Votre plat favori est : {food}")
    food = input("Entrez un autre de vos plats favoris :")

print("Au revoir.")



num = int(input("Entrez un nombre entre 1 et 10 : "))

while num < 1 or num > 10:
    print(f"{num} est inférieur à 1 ou supérieur à 10.")
    num = int(input("Entrez un nombre entre 1 et 10 : "))

print(f"Le nombre choisi est {num}")