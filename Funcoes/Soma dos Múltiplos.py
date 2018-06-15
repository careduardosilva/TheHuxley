def SumNatural(n): #Inicializamos a funcao SumNatural
    i = 0 #Inicializamos as variaveis
    multiplo = 0
    while (i < n): #Daqui para baixo, refere-se as operacoes de obtencao dos multiplos de 3 e 5
        if(i%3 == 0 or i % 5 == 0):
            multiplo += i
        i += 1 #Incrementamos i para nao cair em looping infinito
    return multiplo #Retornamos o valor multiplo para a funcao.
number = int(input())
soma = SumNatural(number) #Aqui guardaremos na soma(variavel), o valor de retorno da variavel multiplo.
print("%d\n"%soma)
#return multiplo, significa que a funcao ira emitir um valor de saida (retorno). 
#return multiplo -> Emita o valor da variavel multiplo
#Assim, para acessarmos o valor da variavel multiplo, basta acessarmos a funcao:
#soma = SumNatural(number) -> Em SumNatural(number) estamos acessando a funcao, quando igualamos a soma, estamos guardando o valor de retorno nessa variavel.
