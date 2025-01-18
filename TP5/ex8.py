import os 

nom_fichier = "exemple.txt"

if os.path.exists(nom_fichier):
    print(f"Le fichier {nom_fichier} existe")
else:
    print(f"Le fichier {nom_fichier} n'existe pas")