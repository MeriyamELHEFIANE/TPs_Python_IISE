class Livre :

    def __init__(self, titre, auteur, annee_pub) :
        self.titre = titre
        self.auteur = auteur
        self.annee_pub =annee_pub

    def __str__(self) :
        return f'Titre : {self.titre} \nAuteur : {self.auteur}\nAnnee de publication : {self.annee_pub}'

class Bibiotheque(Livre) :

    def __init__(self) :
        self.list_livre = []

    # ajouter_livre(livre) pour ajouter un livre à la bibliothèque
    def ajouter_livre(self, livre) :
        if livre not in self.list_livre :
            self.list_livre.append(livre)

    # afficher_livres() pour afficher tous les livres de la bibliothèque
    def afficher_livres(self):
        # vérifier si la bibliothèque est vide ou non
        if self.list_livre == []  :
            print("La bibliothèque est vide !")
        else :
            print("**** Liste des livres ***")
            print("--------------")
            for livre in self.list_livre :
                print(livre)
                print("--------------")



Biblio = Bibiotheque()
Livre1 = Livre("White nights", "Fyodor Dosteovsky" , 1848)
Livre2 = Livre("Les Misérables", "Victor Hugo", 1862)
Biblio.ajouter_livre(Livre1)
Biblio.ajouter_livre(Livre2)
Biblio.afficher_livres()
