import random
a = ["al","bl","vl","tl"]
b = ["sl","dl","fl","gl"]
c = {}
for i in range (len(a)):
    c[a[i]] = b[i]
a = list(c.keys())
s = random.choice(a)
del c[s]
print(c)
