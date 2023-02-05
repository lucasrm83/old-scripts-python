opcao = ''
import sl4a
nome = []
droid = sl4a.Android
while opcao != "x":
    for i in range(50):
        print("")
    print("\n")
    print(" ****************************** ")
    print(" ******* TESTE DE BURRICE ******** ")
    print(" ****************************** ")
    
    print("_________________________________")
    print("___________[1] JOGAR ____________")
    print("__________[2] TUTORIAL ____________")
    print("__________[3] CREDITOS __________")
    print("____________[x] SAIR ___________")
    print("_________________________________")
    opcao = input("   ")
    if opcao == "1":
        nome.append(input("Digite Seu Nome: "))
        print("Bem Vindo", nome[0])
        print("O que é GPU?")
        print("[1] Processador ")
        print("[2] Placa Mãe ")
        print("[3] Placa de Video")
        print("[4] Sensor de luz da camera ")
        print("[5] Nenhuma das questões")
        print("[r] Ver resposta")
        while opcao != "6":
            opcao = input("Digite a Opção:   ")
            if opcao == "1":
                print("Você é muito burro!", nome[0])
            elif opcao == "2":
                print("Você é um jumento!", nome[0])
            elif opcao == "3":
                print("Você não é muito burro", nome[0])
            elif opcao == "4":
                print("você errou seu quadrupide", nome[0])
            elif opcao == "5":
                print("você errou seu jumento burro", nome[0])
            elif opcao == "r":
                print("questao 3", nome[0])
    elif opcao == "2":
        print("TUTORIAL: Você deve fazer a escolha certa para ganhar")
    elif opcao == "3":
        print("Eu")
    elif opcao == "x":
        print("Obrigado por jogar, até a proxima ^^")