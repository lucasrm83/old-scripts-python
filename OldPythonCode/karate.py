import sl4a
import time
import random
vez = 0
droid = sl4a.Android()
lista = ["guedan barái","chudan zuquí","ageuke jodan","soto uke","shuto uke", "jodanzuquí", "uchi uke"]
while True:
    golpe = random.choice(lista)
    if int(vez) % 2 == 0:
        droid.ttsSpeak("avança "+golpe)
    else:
        droid.ttsSpeak("recua"+golpe)
    time.sleep(3)
    droid.ttsSpeak("itch")
    time.sleep(2)
    droid.ttsSpeak("ni")
    time.sleep(2)
    droid.ttsSpeak("san")
    time.sleep(5)
    vez+=1
def menu():
    print(">>>> Auxiliar de Treino <<<<")
    print("[1] Treino de reaçao")
    print("[2] Kihon")