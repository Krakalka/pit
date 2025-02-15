a = input()
d=0
v = "aeoiu"
for i in range(len(v)):
    e = v[i]
    s=a.find(e)
    while s != -1:
        s=a.find(e)
        a = a.replace(e,"",1)
        if s != -1:
            d = d+1
print(d)
