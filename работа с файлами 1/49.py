def lol (a,file):
    f1 = open(file)
    b = f1.readlines()
    s = len(b)
    b = b[s-a:s]
    f1.close()
    print(b)
a = int(input())
while a <= 0:
    a = int(input())
lol(a,"txt.txt")


