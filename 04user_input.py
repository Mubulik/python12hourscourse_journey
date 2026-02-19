#input() = Fonction qui demantde à l'utilisateur d'insérer des données
#          Return les données as string


name = input("Quel est ton nom : ")
age = int(input("Quel âge avez-vous ? : "))

age =+ 1


print(f"Bonjour {name} !") ; print(f"Vous avez {age} ans.")


#Exercice : calculer l'aire d'un rectange avec 2 input donnés.

longeur = float(input("Longeur du rectangle : "))
largeur = float(input("Largeur du rectangle : "))

aire = longeur * largeur

print(f"L'aire du rectange de longeur {longeur}cm et de largeur {largeur}cm, est de {aire}cm²")