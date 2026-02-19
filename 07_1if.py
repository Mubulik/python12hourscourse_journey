# if = Execute du code seulement SI une condition est vérifiée
#      Sinon fait autre chose

age = int(input("Entrez votre age : "))

if age >= 18:
    print("Vous êtes majeur !")
elif age < 0:
    print("MENTEUR")
elif age >=99:
    print("T'es sacrément vieux mon salaud")
else:
    print("Vous êtes mineur...")



response = input("T'as soif? (O/N) : ")
soif = False

if response == "O":
    soif = True
elif response == "N":
    soif =  False
else:
    print("Input non conforme.")



name = input("Entrez votre nom : ")

if name == "":
    print("Le nom ne peut pas être vide")
else:
    print(f"Salut {name} !")