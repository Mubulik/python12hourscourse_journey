# Match-case statement (switch) = Une alternative à l'utilisation de beaucoup de "elif"
#                                 Execute du code si une valeur match a "case"
#                                 Benefices : Plus lisible et une meilleure syntaxe

def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thrusday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _: # _ -> Joker, pour tout cas non mentionné return par défaut
            return "Entrée invalide"

print(is_weekend(input("Entrer un jour de la semaine : ")))