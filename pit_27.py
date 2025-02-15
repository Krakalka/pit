u = 100
s = -1
q = 0
for  i in range(6):
    r = float(input("Введите число от 1 до 99.9: "))
    q = q+r
    if round(r, 2) > s:
        s = round(r, 2)
    elif round(r, 2) < u:
        u = round(r, 2)
d = q/6
print("наибольшее",s,", наименьшее", u)
print(round(q,2), round(d,2))
