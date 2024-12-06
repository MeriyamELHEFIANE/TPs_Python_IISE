class Chien :
    def __init__(self, nom, race, age) :
        self.nom = nom
        self.race = race
        self.age = age
    # aboyer() est une methode pour affiche "Woof!"
    def aboyer(self) :
        print("Woof!")
c1 = Chien("Lona","Berger de Russie",2)
c1.aboyer()