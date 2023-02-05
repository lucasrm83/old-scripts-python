opcao = []
estudante = []
while opcao != "x":
    print("*****MENU*****")
    print("[1] cadastrar estudante")
    print("[2] listar estudantes")
    print("[x] sair")
    opcao = input("Digite a opcao:")
    if opcao == "1":
        estudante.append(input("Digite o nome do estudante:"))
    elif opcao == "2":
        for i in estudante:
            print (estudante)
    elif opcao == "x":
        print("obrigado por usar nossos servicos")