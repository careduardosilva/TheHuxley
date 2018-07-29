gabarito = input()
lista_notas = []
aprovado = 0
while(True):
    entrada = input()
    if(entrada != "9999"):
        nota = 0.0
        entrada = entrada.split()
        numero_aluno = entrada[0]
        respostas_aluno = entrada[1]
        for (i,j) in zip(gabarito,respostas_aluno):
            if(i == j):
                nota += 1.0
        lista_notas.append(nota)
        if(nota >= 6):
            aprovado += 1
        print(numero_aluno+" "+str(nota))
    else:
        dic_notas = dict.fromkeys(lista_notas)
        maior_freq = 0
        for i in lista_notas:
            count = 0
            count = lista_notas.count(i)
            dic_notas[i] = count
        for chave,valor in dic_notas.items():
            if(max(dic_notas.values()) == valor):
                maior_freq = chave
        print("{0:.1f}%".format((aprovado/int(numero_aluno))*100))
        print(maior_freq)
        break
