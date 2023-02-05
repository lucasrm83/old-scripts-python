#Formulas de calculo foram retiradas de https://gamefaqs.gamespot.com/psp/943356-monster-hunter-freedom-unite/faqs/53339
#Para facilitar o cálculo, alguns modificadores foram pré-definidos, mas como resultado o dano final é menos preciso
#Vale lembrar que o dano final também varia com buffs e o tamanho do fio empregam papeis importantes no dano final
#Como fiz esse código a muito tempo, algumas partes não lembrarei bem
ataque = float(input("Atk: "))
#Representa o ataque básico da arma, quanto de dano base ela tem
tipo = 0.33
#Tipo representa o tipo de ataque da arma, que no caso esse é o primero corte com a espada ao pressionar Triângulo
print("Verde  [1]\nAzul   [2]\nBranco [3]\nRoxo   [4]")
fio = 0
#Esse imput pede o nível de afiação da arma
sharp = input("Sharp: ")
if sharp == "1":
    fio = 1.125
if sharp == "2":
    fio = 1.25
if sharp == "3":
    fio = 1.30
if sharp == "4":
    fio = 1.50
d = 0.40
#d é a hitzone a ser atacada
e = 1.0
#e é o modificador de defesa do monstro
f = 1.0
#f é modificador de rage do monstro
g = 1.05
#g é a variável de dano da longsword, cada arma tem o seu, mude caso desece calcular o dano de outro tipo de arma
h = 4.8
#h é o multiplicador da classe da arma
r = (ataque*tipo*fio*d*e*f*g)/h
#Formula de dano fisico
print("Raw:  %.2f" %r)

s = float(input("Element: "))
#Dano elemental da arma
t = 0
#variável pra verificar a afiação da arma
if sharp == "1":
    t = 1.0
if sharp == "2":
    t = 1.0625
if sharp == "3":
    t = 1.25
if sharp == "4":
    t = 1.20
u = float(0.20)
#Fraqueza ao elemento da area a ser atingida
v = float(1.05)
#modificador da longsword
r2 = (s*t*u*v)/10
#calculo dano elemental
print("")
print("")
print("Raw:  %.2f" %r)
#Dano fisico
print("Element: %.2f" %r2)
#dano elemental
final = (r+r2)
print("Total: %.2f " % final)
#dano final