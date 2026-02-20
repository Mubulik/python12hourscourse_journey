# Jeu fait sans aide de la vidéo
# Pierre Feuille Ciseaux en BO3
import random

options = {"P":"Pierre", "F":"Feuille", "C":"Ciseaux"}
choices = ("P", "F", "C")
elements = ("Pierre","Feuille", "Ciseaux")
user_choice = ""
scores = [0, 0]
running = True

print("Bienvenue sur Pierre, Feuille, Ciseaux. Le jeu se joue en 3 manches. Que le meilleur l'emporte !")
print("Pour jouer, il vous sera demander de choisir parmis les choix suivants : ")

for choix, element in options.items():
    print(f"{choix} : {element}")

while scores[0] < 2 and scores[1] < 2:
    to_beat = random.choice(elements)
    user_choice = options.get((input("Entrez votre choix (P/F/C) : ").upper()))

    while user_choice not in choices:
        print("Entrée invalide. Veuillez choisir entre P/F/C.")
        user_choice = options.get((input("Entrez votre choix (P/F/C) : ").upper()))


    if user_choice == to_beat:
        print(f"{user_choice} contre {to_beat} | Egalité ! La manche n'est pas comptée.\n")
        user_choice = ""
    
    elif (user_choice == "Pierre" and to_beat == "Feuille") or (user_choice == "Feuille" and to_beat == "Ciseaux") or (user_choice == "Ciseaux" and to_beat == "Pierre"):
        print(f"{user_choice} contre {to_beat} | Perdu !")
        scores[1] += 1
        print(f"Le score est de {scores[0]} à {scores[1]}.\n")
        user_choice = ""
    
    else:
        print(f"{user_choice} contre {to_beat} | Gagné !")
        scores[0] += 1
        print(f"Le score est de {scores[0]} à {scores[1]}.\n")
        user_choice = ""


print(f"Partie terminée! Voici les scores : \nJoueur : {scores[0]} | Ordinateur : {scores[1]}")
if scores[0] > scores[1]:
    print("Bravo, vous avez remporté la partie !")
else:
    print("Dommage, vous avez perdu.")