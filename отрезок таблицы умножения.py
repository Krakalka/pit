a = int(input())
a1 = int(input())
c = int(input())
c1 = int(input())
print(end = '\t')
for i in range (c,c1+1):
    print(i,end = '\t')
print()
for i in range (a,a1+1):
    print(i,end = '\t')
    for k in range (c,c1+1):
        r = i*k
        print (r,end = '\t')
    print()
