def cylinder():
    u = 0
    i = int( input())
    s = 0
    r = 0
    while i!=0:
        u += i
        s += 1
        i = int( input())
        r = u/s
    return r
print(cylinder())
