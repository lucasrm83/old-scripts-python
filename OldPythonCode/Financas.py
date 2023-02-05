def menu():
    print("\n \n \n \n \n")
    print("-------- Menu --------")
    print("[1] Gravar Devedores")
    print("[2] Ler Devedores")
    print("[3] Checar Conta")
    print("[4] Atualizar Conta")
    print("[x] Sair")
    opcoes = ["1","2","3","4","x"]
    entrada = ''
    while entrada not in opcoes:
        entrada = input("Digite a opcao: ")
        if entrada not in opcoes:
            print("opcao inválida",entrada)
        return (entrada)
        
        
def gravarValor():
    pessoa = input("Pessoa: ")
    valor = input("Valor: ")
    data = input("Data: ")
    motivo = input("Motivo: ")
    arquivo = open("/storage/emulated/0/financas/dados.txt","a")
    arquivo.write(pessoa+" R$:"+valor+" Data:"+data+" Motivo:"+motivo+"\n")
    print("Texto Gravado!")
    arquivo.close()
    
def basicGrav():
    money = input("Valor atual: ")
    arquivo = open("/storage/emulated/0/financas/valor.txt","w")
    arquivo.write(money)
    print("Valor Atualizado!")
    arquivo.close()

def lerBasic():
    arquivo = open("/storage/emulated/0/financas/valor.txt","r")
    texto = arquivo.readlines()
    for i in texto:
        print("R$:",i)
    arquivo.close()
def delValor():
    arq = open('/storage/emulated/0/Financas/dados.txt','r',)
    texto = arq.readlines()
    for i in texto:
        print("null")
  
def lerValores():   
    arq = open('/storage/emulated/0/Financas/dados.txt','r',)
    texto =  arq.readlines()
    for linha in texto : print(linha)
    arq.close()
    
while True:
    opcao = menu()
    if opcao == "1":
        gravarValor()
    elif opcao == "2":
        lerValores()
    elif opcao == "3":
        lerBasic()
    elif opcao == "4":
        basicGrav()
    elif opcao == "x":
        break