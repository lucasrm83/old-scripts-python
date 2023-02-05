import sl4a
repeat = ""
while True:
    droid = sl4a.Android()
    print("[1] falar a verdade")
    print("[2] sair")
    inp = input("")
    if inp == "1":
        droid.ttsSpeak("Tu vai ser reprovada!")
    else:
        droid.ttsSpeak("Tu vai morrer... antes do natal.")