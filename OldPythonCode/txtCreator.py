while True:
    texto = input("Texto: ")
    nome = input("Nome do arquivo: ")
    arquivo = open("/storage/emulated/0/txt/"+nome+".txt","w")
    arquivo.write("\n"+texto)
    print("Texto Gravado! \n")
    arquivo.close()