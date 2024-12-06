class CompteBancaire: 
    def __init__(self, titulaire, solde) :
        self.titulaire = titulaire
        self.solde = solde
    # deposer(montant) pour qui ajouter de l'argent au solde.
    def deposer(self, montant) :
        self.solde += montant
    # retirer(montant) pour retirer de l'argent du solde
    def retirer(self, montant) :
        # vérifiez que le solde est suffisant
        if montant > self.solde :
            print("Votre solde est insuffisant !") #
        else : 
            self.solde -= montant
    # afficher_solde() pour afficher le solde actuel
    def afficher_solde(self) :
        print("Votre solde actuel est :",self.solde)
c1 = CompteBancaire("kjjfjjf",3000)
c1.afficher_solde()
c1.deposer(200)
c1.afficher_solde()
c1.retirer(4000)
c1.afficher_solde()

    
        
