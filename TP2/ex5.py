class Animal :
    def faire_du_bruit(self) :
        return ""
class Chien(Animal) :
    def faire_du_bruit(self) :
        return "Woof !"
class Chat(Animal) :
    def faire_du_bruit(self) :
        return "Miaou !"
ch = Chien()
cha = Chat()
print(ch.faire_du_bruit())
print(cha.faire_du_bruit())