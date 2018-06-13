def MaiorAB(a,b): #Inicializacao da funcao MaiorAB com 2 argumentos.
    return (a+b+abs(a-b))/2
entrada = input().split()
c = int(entrada[2])
a = int(entrada[0])
b = int(entrada[1])
maiorab = MaiorAB(a,b) #PRimeiro, calculamos o maior entre o primeiro e o segundo
maiorabc = MaiorAB(maiorab,c) #Depois, pegamos o maior entre o primeiro e o segundo e calculamos o maior dele com c.
print("%d eh o maior"%maiorabc)
#Exemplo de caso:
#a = 1, b = 2,c = 3
#maiorab = MaiorAB(1,2)
#maiorab = 2
#maiorabc = MaiorAB(2,3)
#maiorabc = 3
