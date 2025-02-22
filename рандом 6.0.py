import random
a = int (input ("№1"))
b = int (input ("№2"))
c = int (input ("off- 1 on- 0"))
if c == 0:
    print(random.random()*(a-b)+b)
elif c == 1:
        print(random.randint(a,b))
