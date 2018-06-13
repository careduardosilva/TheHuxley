def CalculaMulta(velocidade): #Inicializacao da funcao
    MAX_VELOC = 50 #Velocidade limite
    multa = 0
    if(0 <= velocidade and velocidade <= MAX_VELOC): #Primeiro verificamos, se a velocidade esta abaixo do limite
        multa = 0
    elif(velocidade <= MAX_VELOC + MAX_VELOC*0.10): #Se nao estiver, entao comecamos a calcular a multa
        multa = 230.00
    elif(velocidade <= MAX_VELOC + MAX_VELOC*0.20):
        multa = 340.00
    else:
        multa = (velocidade - MAX_VELOC)*19.28
    return multa
veloc = int(input())
multa = CalculaMulta(veloc) #Passamos o argumento veloc para funcao CalculaMulta, e guardamos ovalor de retorno na variavel multra
print("%.2f"%multa)
#MAX_VELOC + MAX_VELOC*0.x0 se refere a velocidade excedida, se no caso for 10%, entao teremos MAX_VELOC + MAX_VELOC*0.10
