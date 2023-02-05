from datetime import datetime




def ler_menu():

   opcoes = ["1","2","3","4","5","x"]

   print()

   print("            BEM VINDO AO E-BAR")



   print()

   print("              [ ]        ")

   print("              |-|       ")

   print("              |_|      ")

   print("              | |     ")

   print("             /   \   ")

   print("            |_____|  ")

   print("            | ___ |  \~~~/    ")

   print("            | \ / |   \_/  \~~~/   ")

   print("            | _Y_ |    |    \_/   ")

   print("            |-----|  __|__   |   ")

   print("            `-----`        __|__")

   print()

   print("         ╔═══════════════════════╗")

   print("         ║» [1] Cadastrar Bebidas║")

   print("         ║» [2] Listar Bebidas   ║")

   print("         ║» [3] Vender Bebidas   ║")

   print("         ║» [4] Listar Vendas    ║")

   print("         ║» [5] Sommelier        ║")

   print("         ║» [x] Sair             ║")

   print("         ╚═══════════════════════╝")

   opcao = ""

   while opcao not in opcoes:

       opcao = input("Digite sua opção: ")

       if opcao in opcoes:

           for x in range(50):

                print()

           return opcao

       else:

           print("Opção inválida: %s" % opcao)

   return None



def cad_bebida():

   print("╔══════════════════════╗")

   print("║  CADASTRO DE BEBIDAS ║")

   print("╚══════════════════════╝")

   codigo = input("\nDigite o codigo: ")

   nome = input("Nome: ")

   estoque = int(input("Estoque: "))

   preco = float(input("Preço: "))

   tipo = input("A bebida e doce ou amarga: ")

   grau = input("A bebida e forte ou fraca: ")

   for x in range(50):

        print()

   return [codigo,nome,estoque,preco,tipo,grau]




def gravar_bebida(bebida):

   arquivo = open("bebidas.txt","a")

   arquivo.write("%s;%s;%d;%.2f;%s;%s;bebida\n" % (bebida[0],bebida[1],bebida[2],bebida[3],bebida[4],bebida[5]))

   arquivo.close()




def ler_bebidas():

   arquivo = open("bebidas.txt","r")

from datetime import datetime









def ler_menu():

   opcoes = ["1","2","3","4","5","x"]

   print()

   print("            BEM VINDO AO E-BAR")









   print()

   print("              [ ]        ")

   print("              |-|       ")

   print("              |_|      ")

   print("              | |     ")

   print("             /   \   ")

   print("            |_____|  ")

   print("            | ___ |  \~~~/    ")

   print("            | \ / |   \_/  \~~~/   ")

   print("            | _Y_ |    |    \_/   ")

   print("            |-----|  __|__   |   ")

   print("            `-----`        __|__")

   print()

   print("         ╔═══════════════════════╗")

   print("         ║» [1] Cadastrar Bebidas║")

   print("         ║» [2] Listar Bebidas   ║")

   print("         ║» [3] Vender Bebidas   ║")

   print("         ║» [4] Listar Vendas    ║")

   print("         ║» [5] Sommelier        ║")

   print("         ║» [x] Sair             ║")

   print("         ╚═══════════════════════╝")

   opcao = ""

   while opcao not in opcoes:

       opcao = input("Digite sua opção: ")

       if opcao in opcoes:

           for x in range(50):

                print()

           return opcao

       else:

           print("Opção inválida: %s" % opcao)





   return None









def cad_bebida():

   print("***CADASTRO DE BEBIDAS***")

   codigo = input("\nDigite o codigo: ")

   nome = input("Nome: ")

   estoque = int(input("Estoque: "))

   preco = float(input("Preço: "))

   tipo = input("Tipo da Bebida: ")

   for x in range(50):

        print()

   return [codigo,nome,estoque,preco,tipo]









def gravar_bebida(bebida):

   arquivo = open("bebidas.txt","a")

   arquivo.write("%s;%s;%d;%.2f;%s;bebida\n" % (bebida[0],bebida[1],bebida[2],bebida[3],bebida[4]))

   arquivo.close()









def ler_bebidas():

   arquivo = open("bebidas.txt","r")

   linhas = arquivo.read().splitlines()

   bebidas = []

   for linha in linhas:

       bebidas_txt = linha.split(";")

       codigo = bebidas_txt[0]

       nome = bebidas_txt[1]

       estoque = int(bebidas_txt[2])

       preco = float(bebidas_txt[3])

       tipo = bebidas_txt[4]

       bebidas.append([codigo,nome,estoque,preco,tipo])

   arquivo.close()

   return bebidas









def listar_bebidas(bebidas):

   for bebida in bebidas:

       print("Codigo: %s" % bebida[0])

       print("Nome: %s" % bebida[1])

       print("Estoque: %d" % bebida[2])

       print("Preco: %0.2f" % bebida[3])

       print("Tipo: %s" % bebida[4])













def recuperar_bebida(codigo):

   bebidas = ler_bebidas()

   for bebida in bebidas:

       if bebida[0] == codigo:

           return bebida

   return None









def existe_bebida(codigo):

   return recuperar_bebida(codigo) != None









def realizar_venda():

   continuar = "s"

   itens = []

   while continuar == "s":

       codigo = input("Digite o codigo da bebida: ")

       bebida = recuperar_bebida(codigo)

       

       if bebida == None:

           print()

           print("Bebida inexistente: %s " % codigo)

           print()

           continue

       print()

       print("Bebida encontrado:\n\t %s" % bebida[1])

       qnt = int(input("Digite a quandidade a ser comprada: "))

       retirar_estoque(codigo, qnt)

       itens.append(codigo)

       print()

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


def retirar_estoque(codigo, qnt):

   bebidas = ler_bebidas()

   for bebida in bebidas:

       if bebida[0] == codigo:

           bebida[2] = bebida[2] - qnt

           break

   arq = open("bebidas.txt", "w")

   for bebida in bebidas:

       gravar_bebida(bebida)

   arq.close()








def listar_vendas():

   vendas = recuperar_vendas()

   print("******* VENDAS *****")

   for venda in vendas:

       print("Venda realizada em: %s " % venda[0])

       codigos = venda[1]

       print("Codigo\t| Nome\t| Estoque\t| Preço\t        | Tipo          ")

       for codigo in codigos:

           bebida = recuperar_bebida(codigo)

           print("| %s\t        | %s\t|%d\t        | %.2f\t| %s\t|\n" % (bebida[0],bebida[1],bebida[2],bebida[3],bebida[4]))







def sommelier():

   tipos = ["destiladas","fermentadas","compostas"]

   print("Oi eu sou o seu Sommelier Virtual :)")

   print("Irei te ajudar a escolher a bebida que se encaixa com o seu gosto")

   print("Qual tipo de bebida você prefere: destiladas, fermentadas ou compostas")

   tipos = input("Eu prefiro bebidas: ")

   if tipos == "destiladas":

       print("As bebidas destiladas são bebidas alcoólicas purificadas através do processo de destilação a partir de uma substância fermentada, como frutas, cereais e outras partes vegetais.")

   elif tipos == "fermentadas":

       print("Bebidas obtidas a partir da fermentação de açúcares existentes nos frutos e cereais pela ação de microorganismos chamados de leveduras.")

   elif tipos == "compostas":

       print("As bebidas alcoólicas feitas pelo processo de infusão, também chamadas bebidas compostas, são obtidas através da imersão temporária de substancias vegetais para que lhes sejam extraídas as essências. ")









while True:

   opcao = ler_menu()

   if opcao == "1":

       bebida = cad_bebida()

       gravar_bebida(bebida)

   elif opcao == "2":

       bebidas = ler_bebidas()

       listar_bebidas(bebidas)

   elif opcao == "3":

       print("***REALIZAR VENDA***")

       print()

       realizar_venda()

   elif opcao == "4":

       listar_vendas()

   elif opcao == "5":

       sommelier()

   elif opcao == "x":

       print("Obrigado!")

       break

   else:

       print("FATAL ERROR!!!!!!! Não era pra ter chegado aqui!!!!!")



