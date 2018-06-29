def SerieMiguelito(indice):
    a1 = 3
    if(indice == 1 or indice == 0): #Caso basico, se o indice for zero ou 1 sabemos que o numero retornado sera o primeiro.
        return a1
    else:
        if(indice % 2 == 0):
            return 4 + SerieMiguelito(indice-1) #Se o indice for par, entao o proximo numero eh dado somando-se 4
        else:
            return 1 + SerieMiguelito(indice-1) #Se o indice for impar, entao o proximo numero eh dado somando-se 1
indice = int(input())
print(SerieMiguelito(indice))
