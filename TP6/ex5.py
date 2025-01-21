def process_input(user_input):
    try:
        n= int(user_input)
        r = 10/n
    except ValueError:
        print("Erreur : Ce n'est pas un nombre valide.")
    except ZeroDivisionError:
        print("Erreur: Division par zero")
    else:
        print(f"Le resultat est {r}.")
process_input(2)