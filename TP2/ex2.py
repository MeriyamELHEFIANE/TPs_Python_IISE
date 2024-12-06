class Voiture :
    def __init__(self, marque, modele, annee) :
        self.marque = marque
        self.modele = modele
        self.annee = annee
    # afficher_info() est une methode qui affiche les information de la voiture
    def afficher_info(self) : 
        print("Marque : ",self.marque,"\nModele : ",self.modele,"\nAnnee : ",self.annee)
v1 = Voiture("Audi", "A5", 2019)
v2 = Voiture("Audi", "A3 SportBack", 2022)
v3 = Voiture("Audi", "Q3", 2023)
v1.afficher_info()
v2.afficher_info()
v3.afficher_info()
