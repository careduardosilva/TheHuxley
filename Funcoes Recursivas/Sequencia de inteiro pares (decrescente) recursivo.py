def decPares(n):
    if(n != 0): #Caso basico para o n
        if(n % 2 == 0): #Se ele for par, printamos
            print(n)
            return decPares(n-1) #Como estamos decrementando n, entao, automaticamente ja mostramos isso em forma decrescente
        return decPares(n-1)
    else:
        return 0
n = int(input())
print(decPares(n))
#Caso de teste:
#n = 4
#-> 4 != 0 -> True
#-> 4 % 2 == 0 -> True
#-> printa(4)
#-> return decPares(4-1)
#-> n = 3
#-> 3 != 0 -> True
#-> 3 % 2 == 0 -> False
#-> return decPares(n-1)
#-> n = 2 
#-> 2 != 0 -> True
#ERROR: ESTOU COM PREGUICA DE CONTINUAR, MAS ENFIM, CONTINUA NESSA SEQUENCIA LOGICA AI
