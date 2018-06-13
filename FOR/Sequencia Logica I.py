n = int(input())
if(0 < n and n < 1000): #Limitamos a entrada
    for i in range(1,n+1): #Iteramos ate n+1
        number = i
        sqr_number = i ** 2 #Quadrado do numero
        cub_number = i ** 3 #Cubo do numero
        print("%d %d %d"%(number,sqr_number,cub_number))
        sqr_number += 1 #quadrado + 1
        cub_number += 1 #cubo +1
        print("%d %d %d"%(number,sqr_number,cub_number))
    
