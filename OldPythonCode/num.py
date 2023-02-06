def calculaRaizQuadrada(numero):
    RAIZ = (1/2)
    resultado = ("%g" %(numero ** RAIZ))
    try:
        resultadoInt = int(resultado) # Se a variável conseguir receber um número inteiro, então ela possui raiz cúbica
        return resultadoInt

    except ValueError:
        return str(resultado)

def calculaRaizCubica(numero):
    RAIZ = (1/3)
    resultado = ("%g" %(numero ** RAIZ))
    try:
        resultadoInt = int(resultado) # Se a variável conseguir receber um número inteiro, então ela possui raiz quadrada
        return resultadoInt

    except ValueError:
        return str(resultado)

a = int(input(""))
b = int(input(""))

# Verifica se 'a' está dentro dos limites do enunciado
if((a < 1) and (a > (10 ** 8))):
    exit()

# Verifica se 'b' está dentro dos limites do enunciado
if((b < a) and (b > (10 ** 8))):
    exit()

cool = 0

for n in range(a, b+1):
    cub = calculaRaizCubica(n) # Calcula os números que possuem raiz cúbica
    if(type(cub) is int): # Se cub tiver raiz cúbica, ele vai verificar se ele também possui raiz quadrada
        qua = calculaRaizQuadrada(n) # Calcula os números que possuem a raiz quadrada
        if(type(qua) is int): # Caso haja raiz quadrada, ele é um número cool
            cool += 1

print(cool)