f1 = open("nums.txt")
b = f1.read()
a=b.split()
b = 0
for i in range(len(a)):
    b = b+int(a[i])
print(b)
f1.close()
