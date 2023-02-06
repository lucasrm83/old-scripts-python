import random
valor = int(input("Valor: "))
aposta = int(input("Aposta: "))
payout = float(input("Payout: "))
payout = payout/100
chance = [1,1,1,1,1,0,0,0,0,0]
tentativas = 0
while True:
	tentativas += 1
	result = random.choice(chance)
	if result == 1:
		valor+=aposta*payout
		if valor >= 1000:
			print("ganhou")
			print("Tentativas: "+str(tentativas))
			break
	if result == 0:
		valor-=aposta
		if valor <= 0:
			print("Perdeu")
			print("Tentativas: "+str(tentativas))
			break
	print('Valor:{:.2f}'.format(valor))

