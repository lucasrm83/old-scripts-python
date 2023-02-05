import time
import androidhelper
droid = androidhelper.Android()
#a = int(input("minuto: "))
#min = a*60
while True:
    time.sleep(60.0)
    droid.vibrate()
    time.sleep(0.5)
    droid.vibrate()
    #droid.ttsSpeak("Um minuto")
    print("#")