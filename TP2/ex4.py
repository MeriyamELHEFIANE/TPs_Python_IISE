class Personne :
    def __init__(self, nom, prenom, age) :
        self.nom = nom
        self.prenom = prenom
        self.age = age
    # se_presenter() pour afficher une présentation de la personne
    def se_presenter(self) :
        print("Je suis",self.prenom, self.nom ,",J'ai" ,self.age,"ans")
p1 = Personne("EL HEFIANE","Meriyam",20)
p1.se_presenter()
class Etudiant(Personne) :
    def __init__(self, nom, prenom, age, matricule, etudier) :
        super().__init__(self ,nom,prenom,age)
        self.matricule = matricule
        self.etudier = etudier
# e1 = Etudiant("m","a",12,"uu","uu")
# e1.se_presenter()
