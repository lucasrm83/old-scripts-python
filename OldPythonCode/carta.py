def contaCorrencias(cidades, cidade):
	cont=0
	for c in cidades:
		if c==cidade:
			cont+=1
	return cont
	

mapa=[]

n=int(input())

for i in range(n-1):
	entrada=input().split(" ")
	mapa.append([int(entrada[0]), int(entrada[1])])

distancia=0
cidadesAndadas=[]

for i in range(len(mapa)):
	atual=mapa[i]
	cidadesAndadas.append(atual[0])
	cidadesAndadas.append(atual[1])
	
	for j in range(len(mapa)):
		if j>i:	
			#print(contaCorrencias(cidadesAndadas, atual[0]))
			if atual[1]==mapa[j][0]:
				if contaCorrencias(cidadesAndadas, atual[0])<=2:
					#cidadesAndadas.append(mapa[j][0])
					#cidadesAndadas.append(mapa[j][1])
					distancia+=1
					break
			elif atual[1]==mapa[j][1]:
				if contaCorrencias(cidadesAndadas, atual[0])<=2:
					#cidadesAndadas.append(mapa[j][0])
					#cidadesAndadas.append(mapa[j][1])
					distancia+=1
					break

if contaCorrencias(cidadesAndadas, mapa[len(mapa)-1][1])<=2:
	distancia+=1
print(distancia)




