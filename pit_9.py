import random
b = int(input("Введите число от 1 до 100: "))
a=0
r=1
s=1
d=100
while a != b :
    a = random.randint(s,d)
    if b > a:
        s = a
        print(a," больше")
        r = r+1
    elif b < a:
        d = a
        print(a," меньше")
        r = r+1
    elif a == b:
        print(a," угадал")
        print("ИИ победил на попытке",r)
c=1
a = random.randint(1,100)
print("теперь черёд ИИ загадывать")
while a != b :
    print("попытка номер",c)
    b = int(input())
    if a > b:
        print("загаданое число больше")
        c = c+1
    elif a < b:
        print("загадоное число меньше")
        c = c+1
    else:
        print("вы угадали на попытке ",c)
if c > r:
    print("ИИ победил раньше")
elif c < r:
    print("Вы победили раньше")
else:
    print("Ничья")
    

    

