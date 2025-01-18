import shutil

source = "journal.txt"
destination = "journal_copie.txt"
deplacer = "archives/"

try:
    shutil.copy(source, destination)
    print(f"Fichier copie de {source} a destination")
except FileNotFoundError:
    print("Le fichier source n'a pas ete trouve.")
except IOError:
    print("Erreur lors de la copie du fichier.")
try:
    shutil.move(source, deplacer)
    print(f"Fichier deplace de {source} a {deplacer}")
except FileNotFoundError:
    print("Le fichier a deplacer n'a pas ete trouve.")
except IOError:
    print("Erreur lors du deplacement du fichier.")

