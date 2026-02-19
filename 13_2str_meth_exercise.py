username = input("Entrez votre nom d'utilisateur : ")

if len(username) > 12:
    print("Le nom d'utilisateur ne doit pas dépasser 12 charachters")
    exit 
elif username.count(" "):
    print("Le nom d'utilisateur ne doit pas contenir d'espace.")
    exit
elif not username.isalpha():
    print("Le nom d'utilisateur ne doit pas contenir de chiffre.")
    exit
else:
    print(f"Bonjour {username} !")