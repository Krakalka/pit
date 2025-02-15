import random
a = []
q = 5
for i in range(q):
    b=[]
    for o in range(q):
        c = random.randint(-10,10)
        if c < 0 :
            c = "-"
        b.append(c)
    a.append(b)
for v in range(q):
    for d in range(q):
        print(a[v][d], end='\t')
    print(end='\n')
print(end='\n\n')
for v in range(q):
    s=0
    for d in range(q):
        g = a[d][v] 
        if g != "-":
            s =s+g
    print(s, end='\t')