c = input("знак ")
a = float(input ("Введите первое число "))
b = float(input("Введите второе число "))
if c =="+":
    print(a+b)
elif c =="/":
    if b != 0:
        print(a//b)
    else:
        print("на ноль делить нельзя")
elif c =="-":
    print(a-b)
elif c =="//":
    if b !=0:
        print(a//b)
    else:
        print("на ноль делить нельзя")
elif c =="*":
    print(a*b,"итог умножения")
elif c =="%":
    if b !=0:
        print(a%b, "остаток от деления")        
    else:
        print("на ноль делить нельзя")

else:
    print("Введите нормальный знак")

