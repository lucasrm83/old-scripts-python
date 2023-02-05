def maiores_valores(lista):

    maiores = [0,0,0]

    for n in notas:

        if n > maiores[0]:

            maiores[2] = maiores[1]

            maiores[1] = maiores[0]

            maiores[0] = n

        elif n > maiores[1]:

            maiores[2] = maiores[1]

            maiores[1] = n

        elif n > maiores[2]:

            maiores[2] = n

    return maiores



notas = [10,4,6,3,7,9]

maiores = maiores_valores(notas)

print("Maiores notas: %d - %d - %d" %(maiores[0],maiores[1],maiores[2]))


a = notas.index(maiores[0])

b = notas.index(maiores[1])

c = notas.index(maiores[2])

print(a,b,c)