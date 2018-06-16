def AnalisarSituacao(nota1,nota2,nota3,nota4): #Definicao da funcao
    media = (nota1*1+nota2*2+nota3*3+nota4*4)/10
    situacao = ""
    if(media >= 9):
        situacao = "aprovado com louvor" #Guardamos a situacao do aluno numa string chamada situacao
    elif(media >= 7):
        situacao = "aprovado"
    elif(3 <= media and media < 7):
        situacao = "prova final"
    elif(media < 3):
        situacao = "reprovado"
    return situacao #Retornamos ela
nota1,nota2,nota3,nota4 = input().split()
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
aluno = AnalisarSituacao(nota1,nota2,nota3,nota4) #Invocamos a funcao AnalisarSituacao, que devolve a string situacao
print(aluno) #Printamos a variavel aluno, que eh a situacao dele.
