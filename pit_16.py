a=5
b=6
c=3
d=4
k = 0
if a>d and c>b:
    c -=1
    d -=1
else:
    a -=1
    b -=1
for i in range(10,100):
    print(i)
    while c >-100 and d>-100:
        k=k+1
        a = c-d
        c=a-b
        d = c-10
        b=a+10
        a = 10-a
        c = 100+a
print(a,b,c,d)
print(k)
