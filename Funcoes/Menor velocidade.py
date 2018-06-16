def velkmh(v0,a,t): #Definicao da funcao velkmh
    return (v0 + a*t)*3.6
v = 0 #Inicializacao das variavei
menorab = 0
for i in range(0,3): #Iremos iterar 3 vezes, isso a fim de evitar criarmos 9 variaveis
    vaux = v #Em vaux, guardamos sempre os valores anteriores de v
    menoraux = menorVAUXeV #Essa variavel vai ser responsavel por guardar os menores valores entre v e vaux. Com o intuito, de usarmos ele no final, para sabermos o menor dos 3.
    v0 = float(input())
    a = float(input())
    t = float(input())
    v = velkmh(v0,a,t) #Podemos obter os menores valores, pela formula do exercicio anterior
    menorVAUXeV = (v+vaux-abs(v-vaux))/2 #Atraves dessa operacao, obteremos os menor valor entre 2. Essa formula eh semelhante a do exercicio anterior chamado "O Maior" favor consultar.
    #A sua respectiva deducao nao me compete. Se vire
menordos3 = (v+menoraux-abs(v-menoraux))/2 #Como menoraux nos dar o menor entre 2 valores, nesse caso sera entre os 2 primeiros,entao, basta fazermos a operacao de obter o menor, novamente.
print("%.1f"%menorabc)
#O Exemplo de caso eh dispendioso, por isso nao irei demonstrar aqui. Sugiro que visitem o site pythontutor.com
