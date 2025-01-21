while True:
    file_name = input("Veuillez saisir le chemin du fichier à lire : ")
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print("\nContenu du fichier lu avec succès")
        print(content)
        break  
    except FileNotFoundError:
        print("Erreur : Le fichier spécifié est introuvable.")
    except PermissionError:
        print("Erreur : Vous n'avez pas les autorisations nécessaires pour lire ce fichier.")
    except Exception as e:
        print(f"Erreur inattendue lors de la lecture du fichier : {e}")
while True:
        try:
            a = int(input("\nVeuillez saisir un entier positif : "))
            if a > 0:
                print(f"\nVous avez saisi l'entier positif : {a}")
                break 
            else:
                print("Erreur : Veuillez saisir un entier positif.")
        except ValueError:
            print("Erreur : Veuillez saisir un nombre entier valide.")


