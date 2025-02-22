import random
a = int(input("1-ая граница "))
b = int(input("2-ая граница "))
if a < b:
    print (random.randint(a,b))
else:
    print (random.randint(b,a))
