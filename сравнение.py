a = input()
a2 = input()
a = a.lower()
a2 = a2.lower()
s = False
if sorted(a) == sorted(a2):
    s = True
print(s)
