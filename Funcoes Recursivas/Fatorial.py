def fatorial(n):
    if(n == 1 or n == 0): #Caso basico, sabemos imediatamente que o resultado do fatorial de n = 1 ou n = 0, eh 1.
        return 1
    else:
        return n*fatorial(n-1)  #Caso contrario, iremos chamar a funcao fatorial n-1 vezes, ate chegarmos no caso basico.
#Inicializacao
n = 0
lines = 0
while(True): #Enquanto for verdadeiro
  n = int(input()) #Vamos pedir o valor de n, varias vezes. Exceto, quando o break for acionado
  if(n != -1 or 0 <= lines <= 12):
    print(fatorial(n)) #Aqui vamos printar o fatorial de cada n dado.
    lines += 1 #Vamos incrementar a quantidade de linhas
    continue #Aqui voltamos pro topo do laco.
  else:
    break
#Caso teste para n = 3: Porem, vamos logo pular para a funcao recursiva, que eh o que queremos entender.
#-> fatorial(3)
#if(n == 1 or n == 0) -> False
#return 3*fatorial(3-1) -> 3*fatorial(2) -> fatorial(2) = 2*1
#-> fatorial(2)
#if(n == 1 or n == 0) -> False
#return 2*fatorial(2-1)
#->fatorial(1)
#if(n == 1 or n == 0) -> True
#return 0
#Se nao entendeu ainda, visite o site pythontutor.com e copie o codigo la.
