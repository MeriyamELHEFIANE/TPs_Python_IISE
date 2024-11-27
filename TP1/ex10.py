def fusionner_dicts(dict1, dict2):
    for cle , val in dict2.items() :
        if cle in dict1 :
            dict1[cle]+=val
        else:
            dict1[cle] = val
    return dict1
dict1={'Pomme':2,'Fraise':3,'Ananas':1}
dict2={'Kiwi':5,'Fraise':1,'Orange':10}
print(fusionner_dicts(dict1,dict2)) # Devrait afficher {'Pomme': 2, 'Fraise': 4, 'Ananas': 1, 'Kiwi': 5, 'Orange': 10}