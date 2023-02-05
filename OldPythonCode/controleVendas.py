from datetime import datetime


def ler_menu():
    opcoes = ["1","2","3","4","x"]
    print("[1] Cadastrar Produto")
    print("[2] Listar produtos")
    print("[3] Vender produto")
    print("[4] Listar Vendas")
    print("[x] Sair")
    opcao = ""
    while opcao not in opcoes:
        opcao = input("Digite sua opção: ")
        if opcao in opcoes:
            return opcao
        else:
            print("Opção inválida: %s" % opcao)
    return None


def cad_produto():
    codigo = input("Digite o codigo: ")
    nome = input("Nome: ")
    estoque = int(input("Estoque: "))
    preco = float(input("Preço: "))
    return [codigo,nome,estoque,preco]

def gravar_produto(produto):
    arquivo = open("produtos.txt","a")
    arquivo.write("%s;%s;%d;%.2f\n" % (produto[0],produto[1],produto[2],produto[3]))
    arquivo.close()

def ler_produtos():
    arquivo = open("produtos.txt","r")
    linhas = arquivo.read().splitlines()
    produtos = []
    for linha in linhas:
        produto_txt = linha.split(";")
        codigo = produto_txt[0]
        nome = produto_txt[1]
        estoque = int(produto_txt[2])
        preco = float(produto_txt[3])
        produtos.append([codigo,nome,estoque,preco])
    arquivo.close()
    return produtos

def listar_produtos(produtos):
    for produto in produtos:
        print("Codigo: %s" % produto[0])
        print("Nome: %s" % produto[1])
        print("Estoque: %d" % produto[2])
        print("Preco: %0.2f" % produto[3])


def recuperar_produto(codigo):
    produtos = ler_produtos()
    for produto in produtos:
        if produto[0] == codigo:
            return produto
    return None

def existe_produto(codigo):
    return recuperar_produto(codigo) != None




def realizar_venda():
    continuar = "s"
    itens = []
    while continuar == "s":
        codigo = input("Digite o codigo do produto: ")
        produto = recuperar_produto(codigo)
        if produto == None:
            print("Produto inexistente: %s " % codigo)
            continue
        print("Produto encontrado:\n\t %s" % produto[1])
        itens.append(codigo)
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
        print("| Codigo\t| Nome\t| Estoque\t| Preço\t|")
        for codigo in codigos:
            produto = recuperar_produto(codigo)
            print("| %s\t| %s\t| %d\t| %.2f\t|" % (produto[0],produto[1],produto[2],produto[3]))







while True:
    opcao = ler_menu()
    if opcao == "1":
        produto = cad_produto()
        gravar_produto(produto)
    elif opcao == "2":
        produtos = ler_produtos()
        listar_produtos(produtos)
    elif opcao == "3":
        realizar_venda()
    elif opcao == "4":
        listar_vendas()
    elif opcao == "x":
        print("Falow!")
        break
    else:
        print("FATAL ERROR!!!!!!! Não era pra ter chegado aqui!!!!!")
