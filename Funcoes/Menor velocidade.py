def velkmh(v0,a,t): #Funcao que calcula velocidade (v0,a,t) sao os argumentos
    return (v0 + a*t)*3.6 #Retornamos o valor dessa operacao ai
v = 0
menorab = 0
for i in range(0,3): #Para nao criarmos 9 variaveis, podemos usar um laço for para repetir as entradas.
    vaux = v
    v0 = float(input()) #Nao, necessariamente, precisamos colocar o nome da variavel igual ao do argumento, pode ser qualquer nome.
    a = float(input()) #Apenas coloquei o mesmo nome, a intuito, de facilitar a compreensao
    t = float(input())
    v = velkmh(v0,a,t) #Retornar significa que a funcao velkmh, quando "INVOCADA" vai retornar o valor da operacao do return.
    menorab = (vaux+v-abs(vaux-v))/2 #Podemos obter os menores valores, pela formula do exercicio "O Maior", a deducao nao me compete.
print("%.1f"%menorab)

#CODIGO EM CONSTRUCAO
