import math

radius = float(input("Entrez le rayon du cercle : "))

circumference = math.pi * 2 * radius
area = math.pi * radius ** 2


print(f"La circonférence du cercle de rayon {radius}cm est de {round(circumference, 3)}cm. Son aire est de {round(area, 3)}cm².5")