import pandas as pd

fichier_csv = "employes.csv"
donnees = pd.read_csv(fichier_csv)

print("Les cinq premières lignes du fichier :")
print(donnees.head())

moyenne_age = donnees['age'].mean()
print(f"\nLa moyenne d'âge des employés est : {moyenne_age:.2f} ans")

# Calculer et afficher la moyenne des salaires
moyenne_salaire = donnees['salaire'].mean()
print(f"La moyenne des salaires est : {moyenne_salaire:.2f} €")