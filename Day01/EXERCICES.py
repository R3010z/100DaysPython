# DAY1/EXERCICES.py — Angela Yu Day 1 (menu interactif + gestion d'erreurs)

def exercice_1():
    """
    Printing Practice (recette) — texte EXACT
    """
    print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
    print("2. Knead the dough for 10 minutes.")
    print("3. Add 3g of Salt.")
    print("4. Leave to rise for 2 hours.")
    print("5. Bake at 200 degrees C for 30 minutes.")

def exercice_2():
    """
    String Manipulation — \n + concat avec espace
    A) 3 lignes avec un seul print
    B) Concaténation avec un prénom (entrée utilisateur)
    """
    # A) retour à la ligne avec \n
    print("Bonjour le monde!\nBonjour le monde!\nBonjour le monde!")

    # B) concaténation avec espace (et entrée utilisateur)
    prenom = input("Entre un prénom pour la salutation : ").strip()
    if prenom == "":
        prenom = "Angela"  # valeur par défaut si l'utilisateur appuie juste Entrée
    print("Bonjour " + prenom)

def exercice_3():
    """
    Debugging Practice — version corrigée (exemple illustratif)
    """
    print("Day 1 - String Manipulation")
    print('String Concatenation is done with the "+" sign.')
    print('e.g. print("Hello " + "world")')
    print("New lines can be created with a backslash and n.")

def exercice_4():
    """
    Input — Hello NOM!
    """
    name = input("What is your name? ")
    print("Hello " + name + "!")

def exercice_5():
    """
    Variables + len() — longueur du nom
    """
    username = input("Quel est ton nom ? ")
    length = len(username)
    print(length)

def exercice_6():
    """
    Swap — échanger glass1 et glass2 sans écrire 'milk'/'juice'
    État final attendu: glass1 = juice, glass2 = milk
    """
    glass1 = "milk"
    glass2 = "juice"

    # Méthode pythonique en 1 ligne (autorisé, sans réécrire les littéraux)
    glass1, glass2 = glass2, glass1

    print("glass1 =", glass1)  # juice
    print("glass2 =", glass2)  # milk

def exercice_7():
    """
    Day 1 Project — Band Name Generator (version simple)
    """
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n").strip()
    pet = input("What's your pet's name?\n").strip()
    print("Your band name could be " + city + " " + pet)

def _menu():
    print("\n=== Day 01 — Menu des exercices ===")
    print("1) Printing Practice (recette)")
    print("2) String Manipulation: \\n + concat")
    print("3) Debugging Practice (version corrigée)")
    print("4) Input: Hello NOM!")
    print("5) Variables + len()")
    print("6) Swap: glass1/glass2")
    print("7) Projet: Band Name Generator")
    print("0) Quitter (ou Entrée vide)")
    return input("Choisis un numéro et appuie Entrée : ").strip().lower()

if __name__ == "__main__":
    try:
        while True:
            choice = _menu()
            if choice in ("0", ""):
                print("Bye 👋")
                break

            try:
                if choice == "1":
                    exercice_1()
                elif choice == "2":
                    exercice_2()
                elif choice == "3":
                    exercice_3()
                elif choice == "4":
                    exercice_4()
                elif choice == "5":
                    exercice_5()
                elif choice == "6":
                    exercice_6()
                elif choice == "7":
                    exercice_7()
                else:
                    print("Choix invalide. Tape 1–7, ou 0 pour quitter.")
            except Exception as e:
                # On n'explose pas le programme si un exo a une erreur : on montre l'erreur et on retourne au menu
                print(f"[Erreur dans l'exercice {choice}] {type(e).__name__}: {e}")

    except KeyboardInterrupt:
        # Ctrl+C / bouton Stop → sortie propre
        print("\nInterruption détectée. Fin du programme 👋")
    except EOFError:
        print("\nEntrée fermée. Fin du programme 👋")
