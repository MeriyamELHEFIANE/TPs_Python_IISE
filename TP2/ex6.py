class Rectangle :
    def __init__(self, largeur, hauteur) :
        self.largeur = largeur
        self.hauteur = hauteur
    # calculer_surface() pour calculer la surface du rectangle
    def calculer_surface(self):
        return "La surface est : {}".format(self.largeur * self.hauteur)
    # calculer_perimetre() pour calculer le périmètre
    def calculer_perimetre(self) :
        return "Le périmètre est : {}".format(2*(self.largeur + self.hauteur))
r = Rectangle(2,4)
print(r.calculer_surface())
print(r.calculer_perimetre())
    