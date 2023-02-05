import sl4a
import time
droid = sl4a.Android()
valor = 0
arquivo = open("/storage/emulated/0/apk/horas.txt","r")
text = arquivo.readlines()
for i in text:
    valor = i
if valor > 60:
    print(valor/60)
arqedit = open("/storage/emulated/0/apk/horas.txt","w")
while True:
    time.sleep(60.0)
    valor+=(1)
    arqedit.write(str(valor))
    if valor > 60:
        print(valor/60)