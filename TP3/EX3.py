from abc import ABC,abstractmethod
import math
class forme (ABC):
    @abstractmethod
    def calculersurface(self):
        pass

class Cercle(forme):
    def __init__(self,rayon) :
        self.rayon = rayon

    def calculersurface(self):
        return math.pi *(self.rayon ** 2)
    
class rectangle(forme) :
    def __init__(self, largeur, hauteur) :
        self.largeur = largeur
        self.hauteur = hauteur

    def calculersurface(self):
        return self.largeur * self.hauteur

class triangle(forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def calculersurface(self):
        return (self.base * self.hauteur) / 2

def afficher_surface(formes):
    for el in formes:
        print(f"Surface: {el.calculersurface()}")

formes = [
        rectangle(5, 10),
        Cercle(3),
        triangle(4, 6)
    ]
afficher_surface(formes)


