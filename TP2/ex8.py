class Personne :

    def __init__(self, nom, prenom, age) :
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.list_amis = []

    def se_presenter(self) :
        print("Je suis",self.prenom, self.nom ,",J'ai" ,self.age,"ans")

    # ajouter_ami(ami) pour ajouter un ami à la liste
    def ajouter_ami(self, ami) :
        # vérifier que l'ami n'existe pas dans la liste
        if ami not in self.list_amis :
            self.list_amis.append(ami)

    # afficher_amis() pour afficher la liste des amis
    def afficher_amis(self) :
        # vérifier si la liste d'amis est vide ou non
        if not self.list_amis :
            print("La liste d'amis est vide !")
        else :
            print("*** Liste des amis ***")
            for ami in self.list_amis :
                print(ami)
            

p1 = Personne("EL HEFIANE","Meriyam",20)
p1.se_presenter()
p1.ajouter_ami("Ahmed EL HEFIANE")
p1.afficher_amis()

