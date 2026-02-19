# for loops = éxecute un bloc de code un nombre de fois fixé
#             Il est possible d'itérer sur une range, string, sequence etc...

# card_number = "1234-5678-9012"
# 
# for x in card_number:
#     print(x)

for x in range(1, 21):
    if x == 13:         # -> on a skip une itération
        continue
    if x == 14:
        break           # -> on arrête la boucle à la condition
    else:
        print(x)
