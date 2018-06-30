def superDigito(numero):
    resultado = 0
    for i in numero:
        i = int(i)
        resultado += i
    resultado = str(resultado)
    if(len(numero) == 1):
        return int(numero[0])
    else:
        if(len(resultado) == 1):
            return int(resultado[0])
        else:
            return superDigito(resultado[0:])
entrada = input().split()
n = entrada[0]
k = int(entrada[1])
x = n*k
print(superDigito(x))
