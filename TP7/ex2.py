import os          # Module pour interagir avec le système d'exploitation
import datetime    # Module pour manipuler les dates et heures
import math        # Module pour les opérations mathématiques

# 1. Afficher le répertoire courant
repertoire_courant = os.getcwd()
print(f"Le répertoire courant est : {repertoire_courant}")

# 2. Afficher la date et l'heure actuelles
maintenant = datetime.datetime.now()
print(f"La date et l'heure actuelles sont : {maintenant}")

# 3. Calculer et afficher la racine carrée d'un nombre donné par l'utilisateur
try:
    nombre = float(input("Entrez un nombre pour calculer sa racine carrée : "))
    racine_carree = math.sqrt(nombre)
    print(f"La racine carrée de {nombre} est : {racine_carree}")
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")