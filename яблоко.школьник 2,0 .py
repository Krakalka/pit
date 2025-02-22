def cylinder():
    r = int(input("r"))
    h = int(input("h"))
    P = 0
    def circle():
        global P
        P = 3,14*r*r
    s = str(input("Бок или всё?"))
    u = r*h
    if s.lower == "бок":
        y = 6.28*u
        print(y)
    elif s.lower == "всё":
        circle()
        t = 6.28*u+P+P
        print(t)
    else:
        print("Comand error") 
cylinder()
