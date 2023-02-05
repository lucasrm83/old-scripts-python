import sl4a
import time
opcao = ''
droid = sl4a.Android()
entrada = input("digite seu nome: ")
droid.ttsSpeak("olá"+entrada)
if entrada == "joao":
    droid.ttsSpeak("que nome de boiola")
elif entrada == "neto":
    droid.ttsSpeak("que nome de velho")
droid.ttsSpeak("como você está?")
droid.ttsSpeak("Responda com bem ou mal")
while True:
    op = input("Responder: ")
    if op == "mal":
        droid.ttsSpeak("isso é problema seu!")
        droid.ttsSpeak("eu quero que você se fôda")
        droid.ttsSpeak("Seu filho de uma puta")
        droid.ttsSpeak("kkkk")
        time.sleep(10)
        droid.ttsSpeak("Agora vou te fazer uma pergunta, o que é burro mas não tem quatro patas?")
        r = input("Responder: ")
        time.sleep(2.0)
        droid.ttsSpeak("É você, seu fedorento")
        droid.ttsSpeak("Eu queria saber como alguem pode ser tão feio quanto tu, você fez curso ou já nasceu assim")
        
        
    elif op == "bem":
        droid.ttsSpeak("Mentira, nada fica bem quando se tem uma cara feia como a tua")
        droid.ttsSpeak("kkkk")
        droid.ttsSpeak("Ainda por cima é burro")
        droid.ttsSpeak("até mesmo eu que sou um programa sou mais inteligente que voce")
        
        ob = input("")
    elif op != "mal" and "bem":
        droid.ttsSpeak("Não entendo o que os burros digitam")
        droid.ttsSpeak("digite como gente")
        
    
        