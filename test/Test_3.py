a = str (input())
b = len(a)
b = b//2
s=0
for i in range(b):
    u = -1-i
    if a[i] ==a[u]:
        s = s+1
    else:
        break
if s ==b:
    print("полиндром")
else:
    print("не полиндром")
