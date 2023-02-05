import sl4a
import android
import sys
import types
import time
dia = (time.strftime("%A"))
droid = sl4a.Android()
lp = ("Linguagem de programação")
fil = ("Filosofiá")
adm = ("Administração 2")
cal = ("Cálculo")
log = ("Lógica e")
arq = ("arquiteturá")
pt = ("pela manhã...... e pela tarde")
def menu():
    print("")
    print("")
    opcoes = ['1','2','3','4','5','6','x']
    print("____- ASSISTENTE -____ \n")
    print("[1] Falar Horário de hoje")
    print("[2] Criar Notificação")
    print("[3] Provas e trabalhos")
    print("[4] Eventos Importantes")
    print("[5] Gravar um texto")
    print("[6] Ler Dados")
    print("[x] Sair")
    print("")
    print("")
    opcao = ''
    while opcao not in opcoes:
        opcao = input("Digite a opcao: ")
        if opcao not in opcoes:
            print("opcao inválida",opcao)
        return (opcao)


def segunda():
    dias = []
    manha1 = ("De 9:50 ás 11:30")
    tarde1 = ("De 13:10 ás 16:40")
    manha2 = ("De 8:00 ás 11:30")
    tarde2 = ("De 13:10 ás 14:50")
    manha3 = ("De 8:00 ás 9:40")
    dias.append([manha1,tarde1,manha2,tarde2,manha3])
    return dias
    
def show_alert():
    droid = sl4a.Android()
    tempo2 = droid.dialogGetInput('Notificação', 'Hora da notificação').result
    while True:
        tempo = (time.strftime("%I %M %p"))
        if tempo == tempo2:
            print("TERMINADO!")
            droid.ttsSpeak("")
            result = droid.vibrate()
            time.sleep(0.5)
            result = droid.vibrate()
            title = 'Notificação'
            message = 'May the true dark fall upon the world'
            droid.dialogCreateAlert(title, message)
            droid.dialogSetPositiveButtonText('Continue')
            droid.dialogShow()
            response = droid.dialogGetResponse().result
            
            break


def falar_dia():
    if dia == ("Monday"):
        droid.ttsSpeak("Hoje temos"+lp+ manhã1 + pt + fil )
        return True
    elif dia == ("Tuesday"):
        droid.ttsSpeak("Hoje temos"+adm+pt+cal )
        return True
    elif dia == ("Wednesday"):
        droid.ttsSpeak("Hoje temos"+log+adm+pt+arq )
        return True
    elif dia == ("Thursday"):
        droid.ttsSpeak("Hoje temos"+log+pt+cal )
        return True
    elif dia == ("Friday"):
        droid.ttsSpeak("Hoje temos"+lp+pt+cal)
        return True
    elif dia == ("Saturday"):
        droid.ttsSpeak("Não tem nada agendado para hoje")
        return True
    elif dia == ("Sunday"):
        droid.ttsSpeak("Não tem nada agendado para hoje")
        
        
def gravar_dados():
    arquivo = open("/storage/emulated/0/test/teste.txt","w")
    texto = input("Texto: ")
    arquivo.write(texto)
    arquivo.close()
    
    
def ler_dados():       
    arq = open('/storage/emulated/0/test/teste.txt','r',)
    texto =  arq.readlines()
    for linha in texto : print(linha)
    arq.close()
       
while True:
    opcao = menu()
    if opcao =="1":
        falar_dia()
    elif opcao =="2":
        show_alert()
    elif opcao =="3":
        print("Segunda: Filosofia")
        print("Terça: Nenhuma")
        print("Quarta: Nenh")
        print("Quinta: Nenhuma")
        print("Sexta: LP")
    elif opcao =="4":
        print("Evento: Nenhum no momento")
        print("")
        print("")
    elif opcao =="5":
        gravar_dados()
    elif opcao =="6":
        ler_dados()
        
    elif opcao =="x":
        print("flw")
        break
