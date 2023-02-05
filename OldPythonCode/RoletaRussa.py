import random
import sl4a
def limpar():
    for i in range(8):
        print("")
limpar()
while True:
    a = input("")
    d = sl4a.Android()
    lista = [0,0,0,1,0,0]
    result = random.choice(lista)
    if result == 1:
        d.vibrate()
        print("Bang!!!")
        limpar()
        break
    else:
        print("Lucky :)")
        limpar()