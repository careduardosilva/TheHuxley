def sum_mult(num,qntd):
    if(qntd == 0): #Teste basico, sabemos que qualquer numero multiplicado por 0, retornara 0
        return 0
    else: 
        if(qntd < 0): 
             return (num + sum_mult(num,abs(qntd)-1))*-1 #Passo recursivo, quando qntd eh negativo, multiplicar por -1 cada numero.
        else:
            return num + sum_mult(num,abs(qntd)-1) #Passo recursivo
#Inicializacao
num1 = int(input())
num2 = int(input())
mult = sum_mult(num1,num2)
print(mult)
