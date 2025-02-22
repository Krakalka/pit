import random
s = []
for j in range (2,11,2):
    a1 = random.randint(0,100)
    for i in range(a1):
        a2 = random.randint(0,len(s))
        a3 = random.randint(0,len(s))
        s.insert(a3,random.randint(0,1))
        s.insert(a2,j)
print(s)
