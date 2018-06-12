entrada = int(input())
tamanho = len(str(entrada)) #Tamanho da entrada
saida = 0
for i in range(0,tamanho): #Iteramos, ate chegarmos no tamanho
    saida += (entrada // 10**i) % 10 #Para entender aqui, veja o exemplo de caso.
print(saida)
#Exemplo de caso:
#entrada = 521
#tamanho = 3 ->Existem 3 caracteres que ocupam 8 bits/1 byte cada.
#saida = 0 #Inicializacao da variavel saida
#Na primeira iteracao:
#i = 0
# saida = (521 // 10**0) % 10 -> saida = (521// 1) % 10 -> saida = 521 % 10 -> saida = 1 + saida(valor anterior da saida, que no caso foi 0)
#Na segunda iteracao:
# saida = (521 // 10**1) % 10 -> saida = (521//10)  % 10 -> saida = 52 % 10 -> saida = 2 + (valor da saida anteirior, que no caso foi 1) -> saida = 3
# saida = (521 // 10**2) % 10 -> saida = (521//100) % 10 -> saida = 5 % 10 -> saida = 5 + (valor da saiada anterior, que no caso foi 3) -> saida = 5 + 3 -> saida = 8
