import random
c= int (input())
a = []
b = 0
u = 0
while c != u:
    u += 1
    a1 = random.randint(1,100)
    print (a1)
    a.append(a1)
    if a1 > b:
        b = a1
a.sort()
print (b)
print(a)

