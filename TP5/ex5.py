import json

with open("etudiants.json", "r", encoding="utf-8") as fichier_json:
    donnees = json.load(fichier_json)

for e in donnees:
    print(f"Nom : {e['nom']}, Âge : {e['âge']}, Note : {e['note']}")
