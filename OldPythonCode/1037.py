entrada = float(input())
if entrada >= 0 and entrada <= 25:
	print('Intervalo [0,25]')

if entrada > 25 and entrada <= 50:
	print('Intervalo (25,50]')

if entrada > 50 and entrada <= 75:
	print('Intervalo (50,75]')

if entrada > 75 and entrada <= 100:
	print('Intervalo (75,100]')

if entrada <0 or entrada > 100:
	print('Fora de intervalo')