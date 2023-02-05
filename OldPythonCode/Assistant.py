import androidhelper
import types
import time
dia = (time.strftime("%A"))
droid = androidhelper.Android()

def ver_user():
    user = ("lucas")
    password = ("0000")
    usuario = ''
    senha = ''
    while usuario != user or senha != password:
        usuario = droid.dialogGetInput('Login', 'Digite o usuario').result
        senha = droid.dialogGetInput('Login', 'Digite o a senha').result
        if usuario == user and senha == password:
            droid.makeToast('Bem vindo, Lucas! :)')
            break
        droid.dialogCreateAlert('Erro!', 'Senha ou usuário inválidos')
        droid.dialogSetPositiveButtonText('Continue')
        droid.dialogShow()
        response = droid.dialogGetResponse().result


    
        
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

    
    
def show_alert():
    message = droid.dialogGetInput('Texto', 'Texto para mostrar').result
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
            droid.notify(title, message)
            droid.dialogCreateAlert(title, message)
            droid.dialogSetPositiveButtonText('Continue')
            droid.dialogShow()
            response = droid.dialogGetResponse().result
            
            break

def semana():
    dias = []
    manha1 = ("De 9 e 50 ás 11 e 30")
    tarde1 = ("Das 13 10 ás 16 40")
    manha2 = ("De 8 00 ás 11 30")
    tarde2 = ("Das 13 10 ás 14 50")
    manha3 = ("De 8 00 ás 9 40")
    dias.append([manha1,tarde1,manha2,tarde2,manha3])
    return dias

def falar_dia():

    lp = ("Elipê")
    fil = ("Filosofiá")
    adm = ("Adêemi 2")
    cal = ("Cálculo")
    log = ("Lógica e")
    arq = ("arquitetúrá")
    pt = ("pela manhã...... e pela tardi")
    if dia == ("Monday"):
        droid.ttsSpeak("Hoje temos"+lp+ pt + fil  )
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
    arquivo = open("/storage/emulated/0/Arquivo/teste.txt","a")
    texto = input("Texto: ")
    arquivo.write("\n"+texto)
    arquivo.close()
    
    
def ler_dados():       
    arq = open('/storage/emulated/0/Arquivo/teste.txt','r',)
    texto =  arq.readlines()
    for linha in texto : print(linha)
    arq.close()
 
#ver_user()       
while True:
    opcao = menu()
    if opcao =="1":
        dias = semana()
        falar_dia()
    elif opcao =="2":
        show_alert()
    elif opcao =="3":
        print("Segunda: Filosofia")
        print("Terça: Nenhuma")
        print("Quarta: ADM II")
        print("Quinta: Calculo")
        print("Sexta: Nenhuma")
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
