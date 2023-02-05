def menu():
	opcoes = ['1','2','3','4','x']
	print("[1] Cadastrar Produto")
	print("[2] Listar Produtos")
	print("[3] Realizar Venda")
	print("[4] Listar Vendas")
	print("[5] Sair")
	opcao = ''
	while opcao not in opcoes:
		opcao = input("Digite a opcao:")
		if opcao not in opcoes:
			print("opcao inválida",opcao)
		return (opcao)
def ler_produto():
	print("**** Cadastro de produto****")
	codigo = input("Digite o codigo do produto:")
	nome = input("Digite o nome do produto:")
	preco = float(input("preco"))
	estoque = int(input("estoque:"))
	produto [codigo,nome,preco,estoque]
	return produto
def existe_produto(produto,codigo):
	for produto in produtos:
		if produto[0] == codigo:
			return True
	return False
def listar_prod(produtos):
	print()
	print("**** listar produtos ****")
	for produtos in produtos:
		print ("Codigo:", produto[0])
		print("Nome:", produto[1])
		print("preco: %.0f" % produto[2])
		print("Estoque: %d" % produto[3])
def recupera_produto(codigo,produtos):
	for produto in produtos:
		if produto[0] == codigo:
			return produto
	return None
def realizar_venda(codigo,produtos):
	produto = recupera_produto(pordutos,codigo)
	print("Venda do produto:   ", produto[1])
	quantidade = int(input("Quantos produtos voce deseja?:"))
	if quantidade <= produto[3]:
		produto[3] = produto[3] - quantidade
		venda = [codigo,quantidade]
		return venda
	else:
		print("Estoque insuficiente")
		return None
produtos = []
vendas = []

while True:
	opcao = menu()
	if opcao == "1":
		produto = ler_produto()
		if ((existe_produto[0],produtos)):
			print ("j� existe um produto com este codigo:")
		else:
			produto.append(produto)
	elif opcao == "2":
		listar_prod(produtos)
	elif opcao == "3":
		codigo = input("informe o codigo do produto")
		if not existe_produto(codigo,produtos):
			print("Não existe nenhum produto com este codigo", codigo)
		else:
			venda = realizar_venda(produtos,codigo)
			if (venda != None):
				venda.append(venda)
	elif opcao == "4":

		print("Listar Vendas:")
	elif opcao == "x":
		print("Obrigado por usar nosso serviço")
		break