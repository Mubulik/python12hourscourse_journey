# Membership operators = utilisé pour tester l'appartenance d'une valeur ou d'une variable dans une séquence
#                        (string, list, tuple, set, or dictionary)
#                        in OU not in
# Idée d'exercice : faire un pendu

# word = "SECRET"
# for char in word:
#     print("*", end="")
# print()
# 
# letter = input("Devinez une lettre dans le mot caché : ")
# 
# if letter not in word:
#     print(f"Loupé ! La lettre {letter} n'est pas dans le mot secret.")
# else:
#     print(f"La lettre {letter} est dans le mot secret.")


notes = {"Jack":10.5,
         "Neuille":19,
         "Fleur":16}

student = input("Entrez le nom d'un étudiant : ")

if student in notes:
    print(f"La note de {student} est {notes[student]}")

