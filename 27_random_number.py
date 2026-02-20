import random

low = 1
high = 6
options = ("pierre","feuille","ciseaux")
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]


# random.randint(1,6)
# number = random.random()
# choice = random.choice(options)

random.shuffle(cards)


print(cards)