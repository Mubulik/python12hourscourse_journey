# List comprehension = Manière concise de créer des lists en Python
#                      Compact est plus lisible qu'une loop traditionelle
#                      [expression for value in iterable if condition]


# Solution avec une loop -> moins efficace
# doubles = []
# 
# for x in range (1,11):
#     doubles.append(x * 2)
# 
# print(doubles)


doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z ** 2 for z in range(1,11)]

print(doubles)
print(triples)
print(squares)
print()


fruits = ["banane", "pomme", "abricot", "peche"]
fruits = [fruit.capitalize() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

print(fruits, fruit_chars)
print()


numbers = [-4, -2, 2, 9, 4]
pos_numbers = [num for num in numbers if num >= 0]
neg_numbers = [num for num in numbers if num <= 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]

print(pos_numbers)

grades = [52, 57, 41, 38, 46, 19, 84, 92]
passing_grades = [grade for grade in grades if grade >= 75]

print(passing_grades)