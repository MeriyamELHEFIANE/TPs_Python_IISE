phrases = []
for i in range(3):
    phrase = input(f"Entrez la phrase {i + 1} : ")
    phrases.append(phrase)

with open("phrases.txt", "w", encoding="utf-8") as fichier:
    for phrase in phrases:
        fichier.write(phrase + "\n")

while True:
    ajout = input("Souhaitez-vous ajouter une phrase ? (oui/non) : ").strip().lower()
    if ajout == "oui":
        phrase = input("Entrez une phrase à ajouter : ")
        with open("phrases.txt", "a", encoding="utf-8") as fichier:
            fichier.write(phrase + "\n")
        print("Phrase ajoutée avec succès.")
    elif ajout == "non":
        print("Ajout terminé. Merci !")
        break
    else:
        print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
