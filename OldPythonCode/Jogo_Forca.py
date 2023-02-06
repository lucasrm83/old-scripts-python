palavra = input("Digite a palavra: ")
erros = 0
lista = []
while True:

    '''for i in palavra:
        print("-")
    '''
    letra =input("Digite a letra: ")
    for i in palavra:
        if letra == i:
            lista.append(letra)
            print(lista)





    else:
        erros += 1

        if erros == 5:
            print("Perdeu! ")
            break






