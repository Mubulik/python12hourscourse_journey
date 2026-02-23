# Remake du dice roller après le weekend de pause, sans aucune aide pour valider les acquis

import random
dice_art = {

    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")

}

user_num = ""
total = 0
dice = []

while not type(user_num) == int:
    user_num = input("Entrez le nombre de dés à lancer : ")
    if user_num.isdigit() == False:
        print("Veuillez entrer une nombre. \n")
    else:
        user_num = int(user_num)

for num in range(user_num):
    dice.append(random.randint(1, 6))

# Solution pour affichage vertical
# for die in dice:
#     total += die
#     for line in range(5):
#         print(dice_art.get(die)[line])


for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()

for num in dice:
    total += num

print(f"Le total des lancés est de {total}.")