class produit:
    def __init__(self,nom,prix) :
        self.__nom = nom
        self.__prix= prix
    @property
    def nom(self):
        return self.__nom
    @property
    def prix(self):
        return self.__prix
    @nom.setter
    def nom(self, new_nom):
        self.__nom = new_nom
    @prix.setter
    def prix(self, new_prix):
        self.__prix = new_prix
    def calculer_prix(self,remise,montant):
        if self.__prix > montant :
            prix_remise = self.__prix * (1 - remise / 100)
            return round(prix_remise, 2)
        return self.__prix
    # Méthode pour afficher les informations du produit
    def afficher(self):
        print(f"Produit: {self.__nom}, Prix: {self.__prix} DH")

p1 = produit("Ordinateur Portable", 1200)
p2 = produit("Casque Audio", 150)
# Affichage des produits
p1.afficher()
p2.afficher()

# Calcul des prix avec remise
print(f"Prix après remise {p1.nom} : {p1.calculer_prix(10, 500)} DH")
print(f"Prix après remise {p2.nom} : {p2.calculer_prix(10, 500)} DH")