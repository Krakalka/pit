def getinput():
    i = input()
    return i
def testinput(i):
    try:
        int (i)
        a = True
        bool(a)
    except:
        a = False
        bool(a)        
    return a
def strToint(i):
    try:
        i=int (i)
    except:
        i = "Error"
    return i
def printint(i):
    print(i)
a = getinput()
print(a)
print(testinput(a))
print(strToint(a))
printint(a)
