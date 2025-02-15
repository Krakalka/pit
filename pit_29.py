import random
def fol():
    a = -10
    lst = []
    for  i in range(100):
        e = random.random()
        e = round(e,2)
        lst.append(e)
    lst.sort()
    for i in range(10):
        a = a + 10
        b = a + 10
        print(lst[a:b])
fol()
