import logging

def log_error(message):
    # Configuration du module logging pour écrire dans un fichier
    logging.basicConfig(filename='error.log', level=logging.ERROR, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Enregistrement du message d'erreur
    logging.error(message)
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        error_message = f"Le fichier '{filename}' n'a pas été trouvé."
        print(error_message)
        log_error(error_message)  # Enregistrement de l'erreur dans le fichier error.log

# Exemple d'utilisation
read_file('fichier_inexistant.txt')