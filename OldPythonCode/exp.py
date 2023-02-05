import random
a = 0
list = []
for i in range(10000000):
    list.append(1)
list.append(0)
print("ok")
while True:
    a += 1
    val = random.choice(list)
    if val == 0:
        break
print(a)