def Len():
    f = "отсанте от меня я шифр кыш уйдите всё конец отстанте"
    s = str(input("slovo: "))
    r = -1
    while s != f :
        r +=1
        f = s[0:r]
    print(r)
Len()
