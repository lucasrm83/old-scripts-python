opcao = ''
nome = []
heroinas = []
while opcao != "x":
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
        print("Escolha a Garota que deseja conquistar: ")
        print("[1] Ana")
        print("[2] Samara")
        print("[3] Misaka")
        print("[4] ")
        print("[5] Shiro")
        print("[6] voltar")
        while opcao != "6":
            opcao = input("Digite a Opção:   ")
            if opcao == "1":
                print("Ana tem cabelo curto sobre os ombros e lindos e profundos olhos castanhos e pele branca como a neve e tem um corpo magro que faria enveja até a modelos ")
            elif opcao == "2":
                print("Samara tem pele morena e cabelos cacheados volumosos, lindos olhos castanhos")
            elif opcao == "3":
                print("Misaka é uma esper level 5, apesar de ser poderosa ainda tem uma amavel e fofa personalidade tsundere. Ela tem olhos e cabelos castanhos curtos sobre os ombros. Um lindo corpo jovem, com certeza a melhor escolha.")
            elif opcao == "4":
                print("")
    elif opcao == "2":
        print("TUTORIAL: Seja bem vindo! o objetivo desse jogo é conquistar a garota que você escolheu, cada uma tem personalidade, vontades e gostos diferentes então é preciso ser muito bom e cuidadoso se quer conquista-las. Primeiro vamos a jogabilidade. No começo do jogo você deve escolher a sua heroina de acordo com o que mais lhe agrada. Os controles são bem simples: Cada uma tem seu proprio diálogo e em cada um voce tera tres opcoes de escolha de resposta enumeradas em [1],[2],[3],[4], e voce devera escolher qual deve usar de acordo com a situação. Você tambem pode sair a qualquer momento digitando x. Boa diversão ")
    elif opcao == "3":
        print("Até o momento os creditos vão somente para mim Lucas Ribeiro ^^")
    elif opcao == "x":
        print("Obrigado por jogar, até a proxima ^^")