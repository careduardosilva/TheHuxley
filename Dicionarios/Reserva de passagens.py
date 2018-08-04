VAGAS = 37
dados_voo= {}
for i in range(VAGAS):
    entrada = input().split()
    num_voo = entrada[0]
    qntd_vaga = entrada[1]
    dados_voo[num_voo] = int(qntd_vaga)
while(True):
    try:
            entrada = input().split()
            num_doc = entrada[0]
            if(num_doc != "9999"):
                num_voo = entrada[1]
                if(dados_voo[num_voo] != 0):
                    print(num_doc)
                    dados_voo[num_voo] = dados_voo[num_voo]-1
                else:
                    print("INDISPONIVEL")
            else:
                break
    except KeyError:
        print("INDISPONIVEL")
