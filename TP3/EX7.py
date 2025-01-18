from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass


class Voiture(Vehicule):
    def deplacer(self):
        return "La voiture roule sur la route."


class Bicyclette(Vehicule):
    def deplacer(self):
        return "La bicyclette est pédalée sur la piste cyclable."


# Exemple d'utilisation
vehicules = [Voiture(), Bicyclette()]

for vehicule in vehicules:
    print(vehicule.deplacer())
