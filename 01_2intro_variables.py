# Test des commentaires, le début d'une nouvelle aventure
print ("Hello World !")
print ("test 101")


# Strings -> suite de caractères
dogo_name = "Lulu"
bouffe = "dentix"
print (dogo_name)
print (f"Bon chien {dogo_name}, tiens un {bouffe} !")

# Integers -> entiers
dogo_age = 4
quantity = 20

print (f"{dogo_name} a {dogo_age} ans.")
print (f"On a acheté {quantity} {bouffe}")

# Floats -> décimales
prix = 9.99
semestre1 = 14.79
distance = 12.4

print (f"Le prix des {bouffe} est de {prix}€.")
print (f"Ma moyenne du premier semestre est de {semestre1}/20")
print (f"La distance Vellefaux - Vesoul est de {distance}km")

# Boolean -> booléen, oui ou non, vrai ou faux
is_student = True

if is_student:
    print("Tu es un étudiant.")
else:
    print("Tu n'es pas un étudiant")