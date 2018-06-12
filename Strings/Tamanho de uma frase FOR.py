#Nesse caso, iremos precisar de um laço FOR ou um while, para podermos iterar por toda string e acumular cada letra numa certa variavel
string = input()
acumulador = 0
if(1 <= len(string) and len(string) <= 500): #Limitacao do tamanho da string
  for i in string: #Iteramos por cada caracter da string e incrementamos o valor do acumulador
    acumulador += 1
 print(acumulador) #Printa na tela
