import random
import sl4a
droid = sl4a.Android()
ver = ('É Verdade')
men = ('É Mentira')
lista = [ver,men]
result = random.choice(lista)
droid.ttsSpeak(result)