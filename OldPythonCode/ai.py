import random
def treino():
    eu = input("Eu: ")
    compl = input("compl: ")
    vontade = input("vont: ")
    fim = input("fim: ")
    if eu == 'x':
        return (False)
    arquivo = open("/storage/emulated/0/Ai/Eu.txt","a")
    arquivo2 = open("/storage/emulated/0/Ai/Complemento.txt","a")
    arquivo3 = open("/storage/emulated/0/Ai/Vontade.txt","a")
    arquivo4 = open("/storage/emulated/0/Ai/Fim.txt","a")
    arquivo.write(eu)
    arquivo2.write(compl)
    arquivo3.write(vontade)
    arquivo4.write(fim)
    arquivo.close()
    arquivo2.close()
    arquivo3.close()
    arquivo4.close()
def conversa():
    arquivo = open("/storage/emulated/0/Ai/Eu.txt","r")
    arquivo2 = open("/storage/emulated/0/Ai/Complemento.txt","r")
    arquivo3 = open("/storage/emulated/0/Ai/Vontade.txt","r")
    arquivo4 = open("/storage/emulated/0/Ai/Fim.txt","r")
    texto = arquivo.readlines()
    texto2 = arquivo2.readlines()
    texto3 = arquivo3.readlines()
    texto4 = arquivo4.readlines()
    a = random.choice(texto)
    b = random.choice(texto2)
    c = random.choice(texto3)
    d = random.choice(texto4)
    print(a,b,c,d)
    arquivo.close()
    arquivo2.close()
    arquivo3.close()
    arquivo4.close()
    
while True:
    entrada = input("Opção: ")
    if entrada == '1':
        while True:
            treino()
    if entrada == '2':
        conversa()
    else:
        break
    