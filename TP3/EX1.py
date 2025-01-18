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

c1 = Cercle(2)
r1 = rectangle(2,4)
print("La surface de cercle est : ",c1.calculersurface())
print("La surface de rectan",r1.calculersurface())