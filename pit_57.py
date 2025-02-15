s = []
s = set(s)
a = 1
while a != "end":
    a = input("Слово конец = end: ")
    b = (a) in s
    if b == False:
        s.append(a)
    elif b == True:
        print("Уже есть")
print(a)