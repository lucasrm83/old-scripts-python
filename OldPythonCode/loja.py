from datetime import datetime






def ler_menu():
    opcoes = ["1","2","3","4","5","x"]
    print()
    print("            BEM VINDO AO ATELIÊ MÃOS DE FADA")
    print()
    print("         ╔══════════════════════════╗")
    print("         ║» [1] Relatório Financeiro║")
    print("         ║» [2] Baixa de Vendas      ║")
    print("         ║» [3] Vender       ║")
    print("         ║» [4] Listar Vendas       ║")
    print("         ║» [5] Sommelier           ║")
    print("         ║» [x] Sair                ║")
    print("         ╚══════════════════════════╝")
    opcao = ""
    while opcao not in opcoes:
        opcao = input("Digite sua opção: ")
        if opcao in opcoes:
            for x in range(50):
                 print()
            return opcao
        else:
            print("Opção inválida: %s" % opcao)
    return None




def cad_bebida():
    print("╔══════════════════════╗")
    print("║  CADASTRO DE BEBIDAS ║")
    print("╚══════════════════════╝")
    codigo = input("\nDigite o codigo: ")
    nome = input("Nome: ")
    estoque = int(input("Estoque: "))
    preco = float(input("Preço: "))
    tipo = input("A bebida e doce ou amarga: ")
    grau = input("A bebida e forte ou fraca: ")
    for x in range(50):
         print()
    return [codigo,nome,estoque,preco,tipo,grau]






def gravar_bebida(bebida):
    arquivo = open("bebidas.txt","a")
    arquivo.write("%s;%s;%d;%.2f;%s;%s;bebida\n" % (bebida[0],bebida[1],bebida[2],bebida[3],bebida[4],bebida[5]))
    arquivo.close()






def ler_bebidas():
    arquivo = open("bebidas.txt","r")
    linhas = arquivo.read().splitlines()
    bebidas = []
    for linha in linhas:
        bebidas_txt = linha.split(";")
        codigo = bebidas_txt[0]
        nome = bebidas_txt[1]
        estoque = int(bebidas_txt[2])
        preco = float(bebidas_txt[3])
        tipo = bebidas_txt[4]
        grau = bebidas_txt[5]
        bebidas.append([codigo,nome,estoque,preco,tipo,grau])
    arquivo.close()
    return bebidas




def listar_bebidas(bebidas):
    print("╔══════════════════════════════╗")
    print("║ Lista de Bebidas Cadastradas ║")
    print("╚══════════════════════════════╝")
    for bebida in bebidas:
        print("Codigo: %s" % bebida[0])
        print("Nome: %s" % bebida[1])
        print("Estoque: %d" % bebida[2])
        print("Preco: %0.2f" % bebida[3])
        print("Tipo: %s" % bebida[4])
        print("Grau: %s" % bebida[5])
        print()
    




def recuperar_bebida(codigo):
    bebidas = ler_bebidas()
    for bebida in bebidas:
        if bebida[0] == codigo:
            return bebida
    return None






def existe_bebida(codigo):
    return recuperar_bebida(codigo) != None






def realizar_venda():
    continuar = "s"
    itens = []
    while continuar == "s":
        print("╔════════════════╗")
        print("║ REALIZAR VENDA ║")
        print("╚════════════════╝")
        codigo = input("\nDigite o codigo da bebida: ")
        bebida = recuperar_bebida(codigo)
        if bebida == None:
            print()
            print("Bebida inexistente: %s " % codigo)
            print()
            continue
        print()
        print("Bebida encontrado:\n\t %s" % bebida[1])
        itens.append(codigo)
        print()
        continuar = input("Continua? [s/n]")
    now = datetime.now()
    data = "%d/%d/%d %d:%d:%d" %(now.day, now.month, now.year, now.hour , now.minute, now.second)
    venda_str = data + ";"
    for i in range(len(itens)):
        venda_str = venda_str + itens[i]
        if i+1 < len(itens):
             venda_str = venda_str + ","
    arq = open("vendas.txt","a")
    arq.write(venda_str+"\n")
    arq.close()








def recuperar_vendas():
    vendas = []
    arq = open("vendas.txt","r")
    linhas = arq.read().splitlines()
    arq.close()
    for linha in linhas:
        if len(linha) == 0:
            continue
        venda = linha.split(";")
        datahora = venda[0]
        codigos = venda[1].split(",")
        vendas.append([datahora,codigos])
    return vendas




def listar_vendas():
    vendas = recuperar_vendas()
    print("******* VENDAS *****")
    for venda in vendas:
        print("Venda realizada em: %s " % venda[0])
        codigos = venda[1]
        print("| Codigo\t| Nome\t\t| Estoque\t| Preço\t| Tipo\t| Grau |")
        for codigo in codigos:
            bebida = recuperar_bebida(codigo)
            print("| %s\t\t| %s\t\t| %d\t\t| %.2f\t| %s| %s|\n" % (bebida[0],bebida[1],bebida[2],bebida[3],bebida[4],bebida[5]))




def sommelier():
    bebidas = ["destiladas","fermentadas","compostas"]
    print("Oi eu sou o seu Sommelier Virtual :)")
    print("Irei te ajudar a escolher a bebida que se encaixa com o seu gosto")
    print("Qual tipo de bebida você prefere: destiladas, fermentadas ou compostas")
    tipo = input("Eu prefiro bebida: ")
    if bebidas == "destiladas":
        bebida = input("Você prefere bebida doce ou amarga: ")
        for bebida in bebidas:
            if bebida == "doce":
                print("A bebida e ",bebida[1])
    elif bebidas == "fermentadas":
        print()
    elif bebidas == "compostas":
        print()
        








   




while True:
    opcao = ler_menu()
    if opcao == "1":
        bebida = cad_bebida()
        gravar_bebida(bebida)
    elif opcao == "2":
        bebidas = ler_bebidas()
        listar_bebidas(bebidas)
    elif opcao == "3":


        realizar_venda()
    elif opcao == "4":
        listar_vendas()
    elif opcao == "5":
        sommelier()
    elif opcao == "x":
        print("Obrigado!")
        break
    else:
        print("ERROR!!!")