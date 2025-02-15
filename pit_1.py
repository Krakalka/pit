import random
a = int(input("Кол-во яблок "))
b = int(input("Кол-во школьников "))
x = random.randint(a,b)
x = x * -1
c = a%b
d = a//b
if a == 0:
    print ("На ноль делить нельзя")
elif a <= -1 or b <= -1:
    print ("Error №",x ,":\nШкольников или яблок слишком мало")
else:
    print (d,"яблок каждому школьнику\n", c, "Осталось в корзине")

