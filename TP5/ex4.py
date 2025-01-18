import csv
with open("contacts.csv", mode="r", encoding="utf-8") as fichier_csv:
    lecteur_csv = csv.DictReader(fichier_csv)
    for ligne in lecteur_csv:
        nom = ligne["Nom"]
        age = ligne["Âge"]
        ville = ligne["Ville"]
        print(f"Nom : {nom}, Âge : {age}, Ville : {ville}")