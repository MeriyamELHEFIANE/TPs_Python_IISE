class Vehicule :
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        print(f"Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}")

class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur
    def afficher_moteur(self):
        print(f"Puissance : {self.puissance}\nType de moteur : {self.type_moteur}")

class Voiture(Vehicule,Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places) :
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places
    def afficher_info(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_moteur(self)
        print(f"Nombre de places : {self.nombre_de_places}")

class Moto(Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto
    def afficher_moteur(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_moteur(self)
        print(f"Type de moto : {self.type_moto}")

voiture1 = Voiture("Tesla", "Model S", 2022, 1020, "Électrique", 5)
moto1 = Moto("Yamaha", "MT-07", 2021, 74, "Essence", "Sport")

voiture1.afficher_info()
print("---")
moto1.afficher_moteur()
        