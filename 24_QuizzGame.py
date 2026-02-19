# Quizz Game

questions = ("Quel est le modpack le plus téléchargé de tout les temps? : ",
             "En quelle version le Hit&Block a-t-il été remplacé par l'arrivée du bouclier? : ",
             "Quel est le serveur français qui a inventé le rush? : ",
             "Dans le mode de jeu Bedwars sur Hypixel, combien coûtent 8 blocs d'obsidienne? : ",
             "Comment s'apelle le plus gros serveur Pvp Faction moddé français? : ")

options = (("A. RL Craft","B. Pixelmon","C. ATM10","D. FTB Beyond"),
           ("A. 1.11","B. 1.7.10","C. 1.9","D. 1.16"),
           ("A. Epicube","B. TheHiveMC","C. Rinaorc","D. Funcraft"),
           ("A. 8 diamants","B. 8 émeraudes","C. 32 lingots d'or","D. 16 lingots d'or"),
           ("A. kFaction","B. PixelmonGo","C. Paladium","D. Athera"))

reponses = ("A", "C", "D", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)

    for option in options[question_num]:
        print(option)
    
    guesses.append(input("Réponse ? (A/B/C/D) : ").upper())
    if guesses[question_num] == reponses[question_num]:
        print("Bonne réponse !")
        score +=1
    else:
        print(f"Loupé ! C'était la réponse {reponses[question_num]}")

    input("\nAppuyez sur une touche pour continuer...\n")

    question_num += 1

print(f"Bonne partie ! Vous avez obtenus un score de {score} !")