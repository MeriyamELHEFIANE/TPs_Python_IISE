def get_positive_integer():
    while True:
        try:
            a = int(input("Veuillez saisir un entier positif : "))
            if a >= 0:
                return a
            else:
                print("Erreur : Veuillez saisir un entier positif.")
        except ValueError:
            print("Erreur : Veuillez saisir un nombre entier valide.")
get_positive_integer()
