with open ("exemple.txt","r") as fichier :
    # enumerate est utilisé pour obtenir le numéro de ligne
    for n, ligne in enumerate(fichier, start=1):
        # La fonction strip() est utilisée pour supprimer les espaces ou sauts de ligne (\n) au début et à la fin de chaque ligne.
        print(f"Ligne {n}: {ligne.strip()}")