import math
a = float(input())
b = float(input())
c = float(input())
delt = (b**2)-4*a*c
print(delt)
raiz = math.sqrt(delt)
x1 = (-b+raiz)/2*a
x2 = (-b-raiz)/2*a
print("R1 = %0.5f"%x1)
print("R2 = %0.5f"%x2)