import math

for i in range(40):
    print("")
print("《《《 Calculadora de Integrais 》》》")
print("")
print("")
a = int(input("Limite Superior: "))

b = int(input("Limite Inferior: "))

n = int(input("Numero de retângulos: "))
print("")


delta = int(b-a)/n

resultadoD = int(0)
resultadoE = int(0)
resultadoM = int(0)
for i in range(n):
    retangulo = (1+i)
    SomaD = delta*math.sin(a+((i+1)*delta))
    resultadoD+=SomaD
    SomaE = delta*math.sin(a+((i)*delta))
    resultadoE+=SomaE
    SomaM = delta*math.sin(a+(delta/2)+((i)*delta))
    resultadoM+=SomaM
print("Retângulo ", retangulo)
print("Ponto da Direita: %.2f " % resultadoD)
print("Ponto da Esquerda: %.2f " % resultadoE)
print("Ponto Médio: %.2f" % resultadoM)
print("_________________________")

