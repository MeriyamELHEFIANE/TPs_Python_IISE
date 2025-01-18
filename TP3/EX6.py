class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"{self.nom} ({self.prix} DH)"


class Commande:
    def __init__(self, produit, quantite):
        if not isinstance(produit, Produit):
            raise ValueError("Le produit doit être une instance de la classe Produit.")
        if quantite <= 0:
            raise ValueError("La quantité doit être supérieure à 0.")
        self.produit = produit
        self.quantite = quantite

    def calculer_total(self):
        return self.produit.prix * self.quantite

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite} = {self.calculer_total()} DH"


class Panier:
    def __init__(self):
        self.commandes = []  # Liste des commandes

    def ajouter_commande(self, commande):
        if not isinstance(commande, Commande):
            raise ValueError("La commande doit être une instance de la classe Commande.")
        self.commandes.append(commande)
        print(f"Commande ajoutée : {commande}")

    def calculer_total(self):
        return sum(commande.calculer_total() for commande in self.commandes)

    def afficher_panier(self):
        if not self.commandes:
            print("Le panier est vide.")
        else:
            print("Contenu du panier :")
            for commande in self.commandes:
                print(f"  - {commande}")
            print(f"Total du panier : {self.calculer_total()} DH")


# Exemple d'utilisation
produit1 = Produit("Pomme", 1.5)
produit2 = Produit("Banane", 2.0)

commande1 = Commande(produit1, 4)
commande2 = Commande(produit2, 3)

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)
panier.afficher_panier()
