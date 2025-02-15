e = int(input("Введите год "))
if e%4 == 0:
    print("visokosni")
elif e % 100:
    if e% 400 == 0 :
        print("visokosni")
    else:
        print("obix")
else:
    print("obix")
