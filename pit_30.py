s = str(input("slovo: "))
w = 0
u = 0
ls = []

while u != -1:
    u = s.find(" ")
    ls.append(s[w:u])
    s = s[u+1:]
    r = len(s[w:u])
    w = u-r
ls.append(s)
print (ls)

