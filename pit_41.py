def un_code(a,b):
    u = ""
    for i in range (len(a)):
        if len(a)!= len(b):
            break
        if a[i] == b[i]:
            u = u +"0"
        else:
            u=u+"1"
    return u 
a = str(input())
b = str(input())
c =un_code(a,b)
d =un_code(c,b)
print (c)
print (d)
