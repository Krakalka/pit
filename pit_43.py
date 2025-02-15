import random
def sus(c,d):
    a = []
    for i in range(10):
        u = random.randint(c,d)
        a.append (u)
    a = tuple(a)
    return a
a = sus(-5,0)
b = sus(0,5)
c = a + b
d = c.count(0)
print(c)
print(d)
