import sl4a
opcao = ''
while opcao != "x":
    droid = sl4a.Android()
    print("TESTE ENEM \n")
    print("Esse teste vai dizer se você vai passar no Enem ou não \n")
    nome = input("Digite seu nome: ")
    idade = int(input("Idade: "))
    signo = input("Signo: ")
    tipo = input("Tipo sanguineo: ")
    if idade != 20:
        print("Sinto muito, você é não vai passar no Enem")
        
        print("_______________________________________________")
        droid.ttsSpeak("Sinto muito, você é não vai passar no Enem")
    elif idade < 25:
        print("Parabéns, você vai passar no Enem! ")
        print("________________________________________________")
        droid.ttsSpeak("Parabéns, você vai passar no Enem! ")