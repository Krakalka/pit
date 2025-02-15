i = " "
while len(i) != 10:
    try:
        i = str(input("Строка"))
        y = len(i)
        if  y <= 10:
            u = 10 - y
            i = i + "*"*u
        elif y > 10:
            print("Cтрока должно быть < или = 10")
    except:
        print("Ошибка при вводе")
print(i)
