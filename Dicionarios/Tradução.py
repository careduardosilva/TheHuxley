while(True):
    entrada = input().split()
    dic_strings = {}
    lista_strings = []
    strings = []
    n = int(entrada[0])
    m = int(entrada[1])
    if(n != 0 and m != 0):
        while(n != 0):
            entrada = input().split()
            lista_strings.append(entrada[0])
            dic_strings.fromkeys(lista_strings)
            dic_strings[entrada[0]] = entrada[2]
            n -= 1
        while(m != 0):
            frase = input()
            frase_split = frase.split()
            for i,j in dic_strings.items():
                if(len(i) != 1):
                    for k in frase_split:
                        if(len(k) >= len(i)):
                            if(i == k[0:len(i)]):
                                frase = frase.replace(i,j)
                else:
                    for k in frase:
                        if(i == k):
                            frase = frase.replace(i,j)
            print(frase)
            m -= 1
    else:
        break
