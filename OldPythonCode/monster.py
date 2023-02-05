import random
import sl4a
d = sl4a.Android()
life = 2000
hp = 300

def menu():
    print("")
    print("")
    opcoes=["1","2","x"]
    print(" >>>> Dragon Slayer <<<<")
    print("[1] Jogar")
    print("[2] Instruções")
    print("[x] Sair")
    print("")
    print("")
    a = input("opcao: ")
    for i in range(20):
        print("")
    
def atack():
    mag = 200
    swd= 300
    flc = 150
    magprob = [0,1,1,1]
    swdprob = [1,1,0,0]
    flcprob = [1,0,1,0,0,1,1,2]
    i= input("Opcao: ")
    if i =! ("1"
    for x in range(20):
        print("")
    if i == "1":
        m = random.choice(magprob)
        if m == 1:
            return (mag)
        else:
           print("errou o golpe!")
           return (0)
    if i == "2":
        s = random.choice(swdprob)
        if s == 1:
            return (swd)
        else:
           print("errou o golpe!")
           return (0)
    if i == "3":
        f = random.choice(flcprob)
        if f == 1:
            return (flc)
        if f == 2:
            print("Crítico!!!")
            return (flc*4)
        else:
           print("errou o golpe!")
           return (0)
        
        
def playSound():
    d.mediaPlay("storage/extSdCard/music/ippo_ost.mp3")

def stopSound():
    d.mediaPlayClose()
    
        
def mon_atk():
    monster = 150
    lista =[0,1,0,0,0,0,2]
    result = random.choice(lista)
    if result == 1:
        d.vibrate()
        return(monster)
    if result == 2:
        d.vibrate()
        time.
    else:
        return(0)
def state():
    if hp <= 0:
        print("Você morreu!")
        stopSound()
        return(False)
    if life <= 0:
        print("Você venceu!")
        stopSound()
        return(False)

    
#playSound()
while True:
    if state() == False:
        break
    menu()
    while True:
        if state() == False:
            break
        state()
        print("Monster: ", life, "        HP: ", hp)
        print("\n")
        print("Magia [1]  Espada [2]  Arco [3]")
    
        op= atack()
        life -=op
        atk= mon_atk()
        hp -=atk