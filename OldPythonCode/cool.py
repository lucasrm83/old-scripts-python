entrada1 = int(input())
entrada2 = int(input())
valor = (entrada2-entrada1)
print(valor)
for i in range(valor):
	cool = 0
	raizQ = entrada1 ** (1/2)
	raizC = entrada2 ** (1/3)
	if ((raizQ ** 2) == entrada1) and ((raizC ** 3) == entrada2):
		cool += 1
print(cool)