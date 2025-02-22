n = 0
w = ""
u = 0
a= "*"
print ("1 = spase; 2= your simb; 3= new line; 4 - delete; 5 - new simb; end = end;"  )
while n != "end":
    n = str(input("print: "))
    if n == "1":
        w = w + " ." 
    elif n== "2":
        w = w + a
    elif n== "3":
        w = w + "\n"
    elif n== "4":
        if u == "2":
            w = w[:-2]
        else:
            w = w[:-1]
    elif n== "5":
        a = input("New simb: ")
        a = a[0]
    elif n== "end":
        break
        w = w.replace(".", " ")
        print (w)
    else:
        print("unnown comand")
    u=n
    print (w)
    w = w.replace(".", "")
    
    
