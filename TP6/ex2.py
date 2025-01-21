def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Erreur : Impossible de convertir '{value}' en entier.")