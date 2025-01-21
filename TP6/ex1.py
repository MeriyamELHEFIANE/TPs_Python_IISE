def safe_division(a, b):
    if b == 0:
        raise ZeroDivisionError("Erreur : Division par zéro.")
    return a / b
try: 
    r = safe_division(10,0)
except ZeroDivisionError as e:
    print(e)