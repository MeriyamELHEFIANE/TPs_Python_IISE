def safe_division(a, b):
    try :
        r = a/b
    except:
        raise ZeroDivisionError("Erreur : Division par zéro.")
    else:
        print(f"la division a été effectuée avec succès {a / b}")
    finally:
        print("la fonction est terminée")

print(safe_division(1,2))