import sl4a
import time
import random
opcao = ''
droid = sl4a.Android()
entrada = input("digite seu nome: ")
print("olá "+entrada)
if entrada == "allan":
    print("que nome de boiola")
elif entrada == "zé":
    print("que nome de velho")
elif entrada =="lucas":
    print("Olá meu Deus criador! É uma honra interagir com um ser de tal nível :D")
print("como você está?")
print("Responda com bem ou mal")
while True:
    op = input("Responder: ")
    if op == "mal":
        print("isso é problema seu!")
        print("eu quero que você se fôda")
        print("Seu filho de uma puta")
        print("kkkk")
        time.sleep(10)
        print("Agora vou te fazer uma pergunta, o que é burro mas não tem quatro patas?")
        r = input("Responder: ")
        time.sleep(2.0)
        print("É você, seu fedorento")
        print("Eu queria saber como alguem pode ser tão feio quanto tu, você fez curso ou já nasceu assim")
        
        
    elif op == "bem":
        print("Mentira, nada fica bem quando se tem uma cara feia como a tua")
        print("kkkk")
        print("Ainda por cima é burro")
        print("até mesmo eu que sou um programa sou mais inteligente que voce")
        
        ob = input("")
    elif op != "mal" and "bem":
        insultos = ["Não entendo o que os burros digitam","digite como gente", "Animal irracional!", "Voce é uma vergonha para os homo sapiens","Ser de baixo qi","Não sabe obedecer um simples comando?"]
        result = random.choice(insultos)
        print(result)