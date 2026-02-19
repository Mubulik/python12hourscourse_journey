# logical operators -> evaluate multiple conditions (or, and, not) ! not = inverse la condition

temp = 25
is_snowing = False
is_sunny = True


if temp < 0 or temp > 5 and is_snowing:
    print("Bataille boule de neige")
else:
    print("caca")


temp2 = 30
is_sunny = True

if temp2 >=28 and is_sunny:
    print("Il fait chaud et beau dehors !")
elif temp2 <= 0 and is_sunny:
    print("Il fait beau mais ça caille sévère")
else:
    print("jsp frr")



# /!\ Comment faire des intervalles : 

if temp2 > 0 and temp2 < 25:
    print("La température est comprise entre 0 et 25")
elif 45 > temp2 > 25:
    print("Canucuuuuule")