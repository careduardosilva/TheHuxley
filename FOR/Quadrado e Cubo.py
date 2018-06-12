lines = int(input()) #quantidade de linhas
if(1 <= lines <= 1000):
    for i in range(1,lines+1): #Iteramos de 1 ate linhas + 1
        number = i 
        square = i**2 #i elevado a 2
        cube = i**3 #i elevado a 3
        print("%d %d %d"%(number,square,cube))
