while True:
    texto = input("Texto: ")
    nome = input("Nome do arquivo: ")
    arquivo = open("/storage/emulated/0/qpython/scripts3/"+nome+".py","w")
    arquivo.write("\n"+texto)
    print("Texto Gravado! \n")
    arquivo.close()