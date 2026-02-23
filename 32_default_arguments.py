# default arguments = valeur par défaut pour certains paramètres
#                     default est utilisé quand un argument n'est pas spécifié lors de l'appel
#                     Cela rend les fonctions plus flexibles, et réduit le nombre d'arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

import time

# def net_price(list_price, discount=0, tax=0.2):
#     return list_price * (1 - discount) * (1 + tax)


# print(net_price(100))
# print(net_price(200, 0.5))
# print(net_price(300, 0.75, 0.1))

def count(end, start=1):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("FINI !")

count(10)