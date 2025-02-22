def lol (fil):
    f1 = open(fil)
    d = []
    n = 0
    b = f1.readlines()
    for i in range(len(b)):
        s = b[i]
        s = s.replace("\n","")
        s = s.split(" ")
        d.append(s)
    for r in range(len(d)):
        for t in range(len(d[r])):
            if len(d[r][t]) > n:
                n = len(d[r][t])
                y = d[r][t]
            elif len(d[r][t]) == n:
                y = y,d[r][t]
    print(y)
    f1.close()
file = "txt.txt"
lol(file)


