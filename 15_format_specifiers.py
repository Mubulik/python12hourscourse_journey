# format specifiers = {value:flag} formatte une valeur en fonction
#                                  des flags renseignés
# 
# .nf = arrondi à n décimales (point fixe)
# :n = alloue n espace
# :03 = allocate and zero pad that many spaces
# :< = justifie à gauche
# :> = justifie à droite
# :^ = aligne au centre 
# :+ = utilise un signe plus pour indiquer une valeur positive
# := = place un signe à la position la plus à gauche
# :  = insère un espace avant des nombres positifs
# :, = coma separator


price1 = 3.1415
price2 = -987.65
price3 = 10000

print(f"Price 1 is {price1:^+,.3f}")
print(f"Price 2 is {price2:^+,.3f}")
print(f"Price 3 is {price3:^+,.3f}")