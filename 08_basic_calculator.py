# Calculatrice basique en python

operator = input("Entrez l'opérateur souhaité (+ - * /) : ")
num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le second nombre : "))

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1-num2 
elif operator == "*":
    result = num1*num2 
elif operator == "/":
    result = num1/num2
else:
     print("L'opérateur sélectionné n'est pas valide.")

print(f"{num1} {operator} {num2} = {result}")