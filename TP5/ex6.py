import os 
ancien_nom = "phrases.txt"
nouveau_nom = "anciennes_phrases.txt"
nom_fichier = "fichier_a_supprimer.txt"

try :
    os.rename(ancien_nom, nouveau_nom)
    print(f"Fichier renomme en {nouveau_nom}.")
except FileNotFoundError :
    print("Le fichier a renommee n'a pas ete trouve.")
except IOError :
    print("Erreur lors du renommage du fichier.")
# Supprimer une fichier 
try :
    os.remove(nom_fichier)
    print(f"Fichier renomme en {nom_fichier}.")
except FileNotFoundError : 
    print("Le fichier a supprimer n'a pas ete trouve.")
except IOError :
    print("Erreur lors de la suppression du fichier")