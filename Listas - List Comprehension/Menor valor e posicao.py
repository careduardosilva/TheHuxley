N = int(input()) #Tamanho Array
numbers = list(map(int,input().split())) #Convertemos cada elemento da lista de string em inteiro
min_value = min(numbers) #Pegamos o menor valor da lista
position = numbers.index(min_value) #Pegamos o indice do menor valor da lista
print("Menor valor: %i" %min_value)
print("Posicao: %i" %position)
#OBS: ATENCAO AO USO DA FUNCAO 'LIST, USAMOS 'LIST(MAP(INT,INPUT().SPLIT()))' PORQUE A FUNCAO MAP, RETORNA UM OBJETO
#DO TIPO MAP, O QUE NAO POSSUI FUNCOES/METODOS QUE PODEMOS APLICAR NAS LISTAS, COMO POR EXEMPLO O 'INDEX'
#POR ISSO EH NECESSARIO CONVERTER O MAP EM UMA LISTA
