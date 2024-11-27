def analyse_texte(texte) :
    mots = texte.split()
    nbre_mots=len(mots)
    nbre_caracteres=len(texte)
    dict1= {"nombre de mots" : nbre_mots,"nombre de caractères" : nbre_caracteres}
    print(dict1)
print(analyse_texte("cours python")) # Devrait afficher {'nombre de mots': 2, 'nombre de caractères': 12}
