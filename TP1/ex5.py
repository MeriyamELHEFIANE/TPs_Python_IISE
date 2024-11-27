def factorielle(n) :
    if n==1 or n==0 :
        return 1
    else :
        return n * factorielle(n-1)
print(factorielle(4)) # Devrait afficher 24