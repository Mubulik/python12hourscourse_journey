# dictionary = collection de pair {clé:valeur}
#              ordonné et changeable. Pas de duplicatats

capitales = {"France":"Paris", 
             "Allemagne":"Berlin", 
             "Japon":"Tokyo",
             "Italie":"Rome", 
             "Belgique":"Frite"}

# print(dir(capitales))
# print(capitales.get("France"))

# for pays in capitales:
#     print(capitales.get(pays))

# if capitales.get("USA"):
#     print("La capitale existe")
# else:
#     print("La capitale n'existe pas.")

# capitales.update({"Espagne":"Madrid"})
# capitales.update({"Italie":"Milan"})

# capitales.pop("Japon") -> retire l'élément spécifié
# capitales.popitem() -> retire le dernier élément du dictionnaire
# capitales.clear()

# keys = capitales.keys()
# values = capitales.values()

# for key in capitales.keys():
#     print(f"La capitale du pays {key} est {capitales.get(key)}")

# items = capitales.items()
# for item in capitales.items():
#     print(item)
# Pour avoir toutes les paires :
# for key, value in capitales.items():
#     print(f"{key} : {value}")