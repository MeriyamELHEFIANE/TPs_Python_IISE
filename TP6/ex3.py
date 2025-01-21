def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print("Contenu du fichier :")
        print(content)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'existe pas.")
    finally:
        # Garantie que le fichier est fermé s'il a été ouvert
        try:
            file.close()
        except NameError:
            # Si le fichier n'a jamais été ouvert, on ignore
            pass

# Exemple d'utilisation
read_file("exemple.txt")
