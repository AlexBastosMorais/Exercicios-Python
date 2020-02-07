lista = []
while True:
    cadastro = input(" Digite 1 para fazer cadastros ou L para acessar a lista de cadastrados: \n")
    if cadastro == "1":

        dados = dict()
        dados ["Nome do usuario:"] = str(input("Digite seu nome:"))
        dados ["Idade do usuario:"] = str(input("Digite sua idade:"))
        dados ["Data de nascimento:"] = str(input("Digite sua data de nascimento:"))
        dados ["E-mail:"] = str(input("Digite seu E-mail:"))
        lista.append(dados)
        print("=-" * 30)
        for k, v in dados.items():
            print(f"  -{k}{v}")

    elif cadastro == "l" or cadastro == "L":
        for nome, idade, data, email in zip (lista):
        print(f"Lista de Cadastrados: ", lista)
        

    elif cadastro == "s" or cadastro == "S":
        break

    elif cadastro != "1" or cadastro != "s" or cadastro != "S" or cadastro != "l" or cadastro != "L":
        print("Comando inválido, tente novamente!")

    
        
       