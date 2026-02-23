# functions = Un bloc de code réutilisable
#             Placer () après une fonction pour l'appeler

def lingangu(placeholder, iteration):
    for i in range(iteration):
        print("Bla Bla Blahh")
        print("Ble Ble Blehh")
        print("Blu Blu Bluuuh")
        print(f"Linganguli Guli-guli-guli {placeholder} Watcha Linganguuu Linganguuu")
        print(i, "\n")

lingangu("PLUUUH", 5)


def display_invoice(username, amount, due_date):
    print(f"Bonjour {username}")
    print(f"Votre facture s'élevant à {amount:.2f}€ est due pour le {due_date}")

display_invoice("Mubulik", 49.99, "24/02/2026")