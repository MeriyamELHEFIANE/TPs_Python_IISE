class Personne :
    def __init__(self,nom,prenom,age) :
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    @property
    def nom(self):
        return self.__nom
    @property
    def prenom(self):
        return self.__prenom
    @property
    def age(self):
        return self.__age
    @nom.setter
    def nom(self, new_nom):
        self.__nom = new_nom
    @prenom.setter
    def prenom(self, new_prenom):
        self.__prenom = new_prenom
    @age.setter
    def age(self, new_age):
        self.__age = new_age


p = Personne("El hefiane","Meriyam",24)
print(p.nom)
print(p.prenom)
p.nom = "hmed"
print(p.nom)
