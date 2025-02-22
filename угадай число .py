import random
a = random.randint(1,100)
b = -1
c = 1
while a != b :
    print("попытка номер",c)
    b = int(input())
    if a > b:
        print("загаданое число больше")
    elif a < b:
        print("загадоное число меньше")
    else:
        print("вы угадали")
    c = c+1
    
    

