import sl4a
arq = open("alunos.txt","r")

opcao = ""
while opcao != "n":
    codigo = input("Codigo: ")
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))  
    arq.write("%s;%s;%s\n" % (codigo,nome,descricao,preco))
    opcao = input("Continuar? [s/n]")
arq.close()
