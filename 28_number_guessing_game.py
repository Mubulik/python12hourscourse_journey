# Jeu du juste prix simplifié, fais sans aide de la vidéo
import random


low = 1
high = 100
to_guess = random.randint(low,high)
guesses = []


print(f"Le nombre à deviner est compris entre {low} et {high}, bonne chance.\n")

while True:
    guess = int(input("Entrez votre guess : "))
    guesses.append(guess)

    if guess > to_guess:
        print("Dommage ! Le guess est trop grand.")
    if guess < to_guess:
        print("Dommage ! Le guess est trop petit.")
    if guess == to_guess:
        print(f"\nFélicitations, tu as gagné, le numéro à deviner était bien {to_guess} !")
        break

print(f"\nVoici tes tentatives ({len(guesses)}) :")
for guess in guesses:
    print(guess, end=", ")
print()