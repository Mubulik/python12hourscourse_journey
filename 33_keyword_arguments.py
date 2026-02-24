# keyword arguments = un argument précédé par un ID
#                     Aide à la lisibilité
#                     L'ordre des arguments n'a pas d'importance

def bonjour(salutation, titre, prenom, nom):
    print(f"{salutation} {titre} {prenom} {nom}")

# bonjour("Bonjour", "BLAH", "Mubulik", "OnSpot") -> Positional argument
# bonjour("Bonjour", nom="BLAH", prenom="YOSHII", titre="pluh") -> Keyword argument, pour mélanger positionel et keyword, il faut mettre en premier les positionels et ensuite les keyword

# print("1", "2", "3", "4", "5", sep="/") # -> sep est un keyword de la fonction print

def get_phone(country, area, phone):
    return f"+{country}{area}{phone}"

phone_num = get_phone(country=33, area=384, phone=567890)
print(phone_num)