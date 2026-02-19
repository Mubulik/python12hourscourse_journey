# collection = "variable" unique pour stocker plusieurs valeurs
#   List  = [] ordonnée et changeable. Duplicatat OK
#   Set   = {} non ordonnée et invariable, mais Ajouter/Supprimer OK. Pas de duplicatat
#   Tuple = () ordonnée et inchangeable. Duplicatat OK, la plus RAPIDE

legumes = ["concombre", "courgette", "carotte", "patate"]
# print(dir(legumes))
# print(help(legumes))
# print(len(legumes))
#print("haricot" in legumes)

# legumes[0] = "haricot"
# legumes.append("haricot")
# legumes.remove("patate")
# legumes.insert(0, "haricot")
# legumes.sort()
# legumes.reverse()
# legumes.clear()
# print(legumes.index("courgette"))
# print(legumes.count("concombre"))


# print(legumes)
# for legume in legumes:
#     print(legume)



fruits = {"tomate", "fraise", "framboise", "abricot", "pêche", "cerise"}

# fruits.add("noix")
# fruits.remove("tomate")
# fruits.pop() # -> retire la première valeur, aléatoire ici
# fruits.clear()

# print(fruits)


feculents = ("patate", "beans", "noix", "pates", "patate")

print(feculents.count("patate"))