def compte_occurences(liste) :
    mon_dict={}
    for i in liste :
        if i in mon_dict :
            mon_dict[i] += 1
        else :
            mon_dict[i] = 1
    print(mon_dict)
compte_occurences(["Pomme","Fraise","Orange","Fraise"]) # Devrait afficher {'Pomme': 1, 'Fraise': 2, 'Orange': 1}

