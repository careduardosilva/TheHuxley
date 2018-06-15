#A questao nao informa se eh juros compostos ou simples, deixa o problema para o usuario. 
entrada = input().split()
capital = float(entrada[0])
juros = float(entrada[1])
anos = int(entrada[2])
montante = capital #No comeco das operacoes, precisamos igualar o montante ao capital, pois se nao o fizer, iremos operar sobre o montante com valor inicial 0, o que complicaria o calculo do rendimento
#ja que usamos a variavel aux e igualamos ela ao montante.
trimAnos = int((12*anos)/3) #Obtem a quantidade de trimestres que tem o ano
aux = 0
for anos in range(1,trimAnos+1): #A funcao range so vai iterar ate trimAnos-1, para evitar isso, adicionamos +1
    aux = montante #Devemos armazenar o montante numa variavel auxiliar para calcular o rendimento
    montante = capital*(1+juros)**anos
    rendimento = (montante - aux) 
    print("Rendimento: %.2f Montante: %.2f"%(rendimento,montante))
#Atente-se sobre o problema de aritmetica de ponto flutuante, eh um topico que seria interessante a leitura.
