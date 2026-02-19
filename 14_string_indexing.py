# indexing = accéder aux éléments d'une séquence en utilisant [] (indexing operator)
#            [start : end : step]

card_number = "1234-5678-9012-3456"

# print(card_number[0])
# print(card_number[:4])
# print(card_number[5:9])
# print(card_number[5:])
# print(card_number[-4])
# print(card_number[::4])

last_digits = card_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reversed_card_number = card_number[::-1]
print(reversed_card_number)