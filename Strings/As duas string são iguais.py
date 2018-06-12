string1 = input()
string2 = input()
is_Equal = string1.lower() == string2.lower() #Se elas forem iguais em minusculo, entao armazena True na variavel is_Equal, caso contrario False.
if(is_Equal and (len(string1) <= 50 and len(string2) <= 50)): #Se is_Equal eh True E o tamanho da string1 for menor ou igual que 50 E o tamanho da string2 menor igual a 50, entao:
    print("IGUAIS") #Printa iguais.
else:
    print("DIFERENTES")
