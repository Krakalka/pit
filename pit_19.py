def krug():
    try:
        r = int(input())
        u = 3,14*r**2
    except:
        print("vvedite chislo")
def kvadrat():
    try:
        a = int(input())
        b = int(input())
        u = a*b
    except:
        print("vvedite chislo")
def treugolnik():
    try:
        a = int(input())
        h = int(input())
        u=0.5*h*a
    except:
        print("vvedite chislo") 
def Choosing():
    a = input(" 1 - krug \n 2-kvadrat \n 3- treugolnik\n")
    if a == 1:
        krug()
    elif a == 2:
        kvadrat()
    elif a == 3:
        treugolnik()
    else:
        print("error 404")
Choosing()
