#conditional expression = Raccourci d'une ligne pour le if-else (ternary operator)
#                         Print ou assigne une des deux valeurs en fonction d'une condition
#                         X if condition else Y


num = -6
a = 6
b = 7
age = 20
temp = 30
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "PAIR" if num % 2 == 0 else "IMPAIR"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Majeur" if age >=18 else "Mineur"
# temps = "CHAUD" if temp >=30 else "FROID"
access_level = "Full Access" if user_role == "admin" else "Basic Access"

print(access_level)