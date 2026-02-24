# Iterables = Un objet/collection qui peut renvoyer ses éléments uns par uns,
#             lui permettant d'être itéré dans une loop

dictionary = {"France":"Paris", 
             "Allemagne":"Berlin", 
             "Japon":"Tokyo",
             "Italie":"Rome", 
             "Belgique":"Frite"}


for key in dictionary.keys():
    print(key)

print()

for values in dictionary.values():
    print(values)

print()

for key, values in dictionary.items():
    print(f"Pays : {key} /// Capitale : {values}")