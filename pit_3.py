import random
a = []
b = 0
for i in range (10):
    a1 = random.randint(1,100)
    print (a1)
    a.append(a1)
    if a1 > b:
        b = a1
a.sort()
print (b)
print(a)

