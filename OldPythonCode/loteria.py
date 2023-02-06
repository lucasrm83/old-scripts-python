# -*- coding: cp1252 -*-
import random; # importar as funcoes do random
# realização dos sorteios
numero = input ("informe a dezena: ")
pessoas = int(input("Número de pessoas: "))
tentativas = 0
while True:
    tentativas+=1
    sorteio = random.randint(1,pessoas)
    if sorteio == numero:
        print("Você Ganhou! ")
        break
    print(tentativas)
