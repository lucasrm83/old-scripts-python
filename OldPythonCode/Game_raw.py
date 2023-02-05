opcao = ''
nome = []
while opcao != "x":
    print("\n")
    print(" ****************************** ")
    print(" ******* JOGO DA MORTE ******** ")
    print(" ****************************** ")
    
    print("_________________________________")
    print("___________[1] JOGAR ____________")
    print("__________[2] TUTORIAL ____________")
    print("__________[3] CREDITOS __________")
    print("____________[x] SAIR ___________")
    print("_________________________________")
    opcao = input("Digite a Opção:   ")
    if opcao == "1":
        nome.append(input("Digite Seu Nome: "))
        print("Bem Vindo", nome[0])
        print("Quanto é 2+3×5?")
        print("[1] = 25 ")
        print("[2] = 30 ")
        print("[3] = 17 ")
        print("[4] = 15 ")
        print("[5] = 0")
        while opcao != "6":
            opcao = input("Digite a Opção:   ")
            if opcao == "1":
                print("Você morreu!")
            elif opcao == "2":
                print("Você morreu!")
            elif opcao == "3":
                print("Você passou!")
                    while opcao != "6":
                        print("O que significa DNA?")
                        print("[1] Acido desoxirribonucleico ")
                        print("[2] Donate nox armanium")
                        print("[3] Acido normal descrito")
                        print("[4] Deuterio no Axonio ")
                        print("[5] Nenhuma")
            elif opcao == "4":
                print("você morreu!")
            elif opcao == "5":
                print("você morreu!")
    elif opcao == "2":
        print("TUTORIAL: Você deve fazer a escolha certa para ganhar")
    elif opcao == "3":
        print("Eu")
    elif opcao == "x":
        print("Obrigado por jogar, até a proxima ^^")