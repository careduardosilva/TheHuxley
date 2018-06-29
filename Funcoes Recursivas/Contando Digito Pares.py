def ContaDigitoPares(numero): 
    i = len(numero) #Guardamos o tamanho da string dada (entrada), assim, poderemos acessar o ultimo numero da string usando (i-1)
    if(i != 0): #So devemos continuar a chamada recursiva, caso a entrada seja diferente de zero
        if(int(numero[i-1]) % 2 == 0): #Convertemos o ultimo elemento da string (ultimo numero), em um inteiro e verificamos se ele eh par
            return 1 + ContaDigitoPares(numero[0:i-1]) #Caso seja, retornamos 1 e continuamos a chamada recursiva. Caso ache novamente um numero par, sera incrementado +1
        else: 
            return ContaDigitoPares(numero[0:i-1]) #Caso contrario, continuamos a chamada recursiva, porem nao acrescentamos 1
    else: #Caso contrario, retornamos 0
        return 0
entrada = input()
print(ContaDigitoPares(entrada))
#PRESTA ATENCAO AQUI:
#Note que a chamada recursiva acontece nas linhas 5 e 7.
#OBS: Lembre do slicing que aprendemos em strings e agora prossiga a leitura abaixo
#Note, tambem, que "numero[0:i-1]" a cada chamada da funcao ele sempre estara decrementando recursivamente, assim
#Estaremos sempre diminuindo o tamanho da string em 1 e analisando o ultimo elemento dessa string, veja a seguir o que quero dizer:
#entrada = "123553"
#A cada chamada recursiva, iremos diminuir a string em 1:
#Na primeira chamada: entrada = "123553"
#Na segunda chamada: entrada = "12355"
#Na terceira chamada: entrada = "1235"
#Na quarta chamada: entrada = "123"
#E assim, por diante, ate chegarmos no ultimo elemento.
#A recursao acontece, devido que estamos sempre invocando a propria funcao para realizar um objetivo e sempre resolvendo um caso basico.
#Caso de teste:
#entrada = "215"
#print(ContaDigitoPares(entrada))
#->i = 3
#-> 3 != 0 -> True
#-> 5 % 2 == 0 -> False #OBS, O 5 se refere ao ultimo digito da string entrada("215")
#-> return ContaDigitoPares("21")
#-> i = 2
#-> 3 != 0 -> True
#-> 1 % 2 == 0 -> False
#-> return ContaDigitoPares("2")
#-> i = 1
#-> 1 != 0 -> True
#-> 2 % 2 == 0 -> True
#-> return 1 + ContaDigitoPares("") -> Isso quer dizer que a funcao vai retornar 1, ja que o argumento de contadigitopares eh nulo e a funcao vai retornar 0
#-> i = 0
#-> 0 != 0 -> False
#-> return 0
