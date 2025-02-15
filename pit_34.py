s = str(input())
u = len(s)
t=0
f=0
for e in range(u):
    w = s[e].islower()
    if s[e] == " ":
        print()
    elif w == False:
        f +=1
    elif w == True:
        t +=1 
if t > f:
    s = s.lower()
elif f > t:
    s = s.upper()
print(s)
