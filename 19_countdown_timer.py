# Création d'un countdown pour un nombre de secondes donné
import time

user_input = int(input("Combien de temps pour le countdown? (s) : "))

for i in range(user_input, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int((i / 3600))
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Fini !")