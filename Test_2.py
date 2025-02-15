a=1
while a !=0:
    a =int (input("o - end"))
    for i in range (a+1):
        for k in range (a+1):
            r = i*k
            print(r,end="\t")
        print("\n")
