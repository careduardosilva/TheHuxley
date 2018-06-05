n = int(input())
for i in range(0,n): #O bloco abaixo sera exeuctado n vezes
    string = input()
    if(len(string) <= 255): #Limita o tamanho da string
        string = string.replace(" ","") #Troca os espacos por nada(character nulo), ja que quando for invertida a string, os espacos podem atrapalhar
        string = string.lower() #Atrapalha quando a string for invertida, por isso devemos deixar ou tudo maiusculo ou tudo minusculo, nesse caso minusculo
        if(string == string[::-1]): #Compara a string normal com a invertida, se forem iguais sao palindromos.
            print("SIM")
        else:
            print("NAO")
