x,y = input().split()
x = int(x)
y = int(y)
if((1 <= x <= 20) and (x <= y <= 100000 )):
    for i in range(1,x+1):
        if(i % x != 0): #Enquanto i não for divisivel por x -> imagine que -> i/x -> 1/8,2/8,3/8... 
            #Percebe que nao so precisamos pular uma linha quando i = 8 ou i = x?
            print("%d"%i,end = " ") #Apenas printamos i e colocamos espaço
        else: #Entao eh aqui que ocorre o pulo, quando i % x == 0, ou i = 8
            print("%d"%i)
            for j in range(x+1,y+1): #Dai iteramos de x+1, ate y+1. Lembre que nao podemos comecar com 8 novamente.
                if(j % x != 0): #Mesma logica que acima acontece aqui.
                    print("%d"%j, end = " ")
                else:
                    print("%d"%j)
