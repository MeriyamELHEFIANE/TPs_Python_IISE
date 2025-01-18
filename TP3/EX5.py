class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, Salaire: {self.salaire} DH"


class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.equipe = []  

    def ajouter_employe(self, employe):
        if isinstance(employe, Employe) and employe not in self.equipe:
            self.equipe.append(employe)
            print(f"{employe.prenom} {employe.nom} a été ajouté à l'équipe.")
        else:
            print("Erreur : L'employé est déjà dans l'équipe ou n'est pas valide.")

    def afficher_equipe(self):
        if not self.equipe:
            print("Aucun employé supervisé.")
        else:
            print("Équipe supervisée :")
            for employe in self.equipe:
                print(f"  - {employe.prenom} {employe.nom}")


# Exemple d'utilisation
e1 = Employe("EL HEFIANE", "Meriyam", 2500)
e2 = Employe("BABA", "Farah", 2800)
m = Manager("AHBRI", "Jihad", 4000)

print(m.afficher())
m.ajouter_employe(e1)
m.ajouter_employe(e2)
m.afficher_equipe()
