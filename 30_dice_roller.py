# Lanceur de dé
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

dice = []
total = 0
num_of_dice = int(input("Entrez le nombre de dés à lancer : "))
print()

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# for line in range(5):
#     print(dice_art.get(dice[0])[line])        /!\ Note : un appel dans le dictionnaire prend le type de la valeur reçue ! 
#                                                          Exemple ici -> dice_art.get(1) est un tuple


for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()


for die in dice:
    total += die

print(f"\nLe total est : {total}")

