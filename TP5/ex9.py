try:
    with open('exemple.txt', 'r') as f:
        lignes = f.readlines()

    # Calculer le nombre total de lignes, de mots, et de caractères
    nombre_lignes = len(lignes)
    nombre_mots = sum(len(ligne.split()) for ligne in lignes)
    nombre_caracteres = sum(len(ligne) for ligne in lignes)

    print("Statistiques du fichier:")
    print(f"- Nombre total de lignes       : {nombre_lignes}")
    print(f"- Nombre total de mots         : {nombre_mots}")
    print(f"- Nombre total de caractères   : {nombre_caracteres}")

except FileNotFoundError:
    print(f"Erreur : Le fichier '{'exemple.txt'}' n'existe pas.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")