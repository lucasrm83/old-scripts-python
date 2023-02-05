import sl4a
repeat = ""
while True:
    droid = sl4a.Android()
    mensagem = input("O que quer falar?   ")
    if mensagem == "":
        droid.ttsSpeak(repeat)
        continue
    droid.ttsSpeak(mensagem)
    repeat = mensagem
