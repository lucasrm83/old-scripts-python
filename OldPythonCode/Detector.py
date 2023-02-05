import random
import sl4a
d = sl4a.Android()
lista = [1,0,0,1]
result = random.choice(lista)
def limpar():
    for i in range(8):
        print("")
limpar()
if result == 1:
    d.vibrate()
    print("Verdade!")
    d.mediaPlay("storage/sdcard0/Android/qpython/verdade.mp3")
    limpar()
else:
    print("Mentira!")
    d.mediaPlay("storage/sdcard0/Android/qpython/mentira.mp3")
    d.vibrate()
    limpar()