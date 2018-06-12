t = int(input())
i = 0
while(i < t and t <= 40): #Limitamos os casos de testes para 40 no maximo e determinamos que executaremos o bloco abaixo "t" vezes
#Primeira iteracao, i = 0
    try: #Error handling
        buracos = 0 #Inicializamos a variavel buraco
        palavra = input() #Pedimos para o usuario digitar a entrada
        for letra in palavra: #Primeira iteracao no caso da palavra
        #letra = primeira letra da palavra
            if(letra == "B"): #Se letra for igual a b, adiciona dois buracos
                buracos += 2
            elif(letra == "A" or letra == "O" or letra == "P" or letra == "R" or letra == "D" or letra == "Q"): #Nos outros casos, adiciona 1
                buracos += 1
        print(buracos) #printa os buracos
        i += 1 #Incrementamos i, para nao acontecer looping infinito
        buracos = 0 #Zeramos o numero de buracos, para que nao continue somando com os anteriores.
    except EOFError: #Caso aconteca o EOFError, quebra o laco
        break
