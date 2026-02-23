# return = instruction utilisée à la fin d'une fonction
#          renvoie un résultat lors de l'appel

# def add(x, y):
#     result = x + y
#     return result
# 
# def subtract(x, y):
#     result = x - y
#     return result
# 
# def multiply(x, y):
#     result = x * y
#     return result
# 
# def divide(x, y):
#     result = x / y
#     return result
# 
# print(divide(1, 2))

def create_name(prenom, nom):
    prenom = prenom.capitalize()
    nom = nom.capitalize()

    return prenom + " " + nom

print(create_name("Mubulik", "TEA"))