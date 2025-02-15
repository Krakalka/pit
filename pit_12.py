a = str(input())
d = len(a)-1
r = len(a)
c = 1
b = ''
if len(a)==0:
    print ("type something")
elif len(a)==1:
    b = b +a+str(c)
else:
    for i in range(0,d):
        if a[i]==a[i+1]:
            c +=1
        elif a[i]!=a[i+1]:
            b = b + a[i]+str(c)
            c = 1
    if i == d:
        b = b + a[r]+str(c)
print(b)
