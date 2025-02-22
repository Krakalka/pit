import random
a = random.randint(1,3)
v1 = "Сколько цветов в радуге?(ответ буквами)"
v2 ="Откуда растения получают энергию?"
v3 = "Сколько элементов в таблице мендилеева?(цифрами)"
if a == 1 :
    a = random.randint(1,2)
    ans1 = input(v1)
    if a == 1 :
        ans2 =input(v2)
        ans3 = input(v3)
    elif a == 2:
        ans3 =input(v3)
        ans2 =input(v2)
elif a == 2 :
    a = random.randint(1,2)
    ans2 =input(v2)
    if a == 1 :
        ans3 = input(v3)
        ans1 = input(v1)
    elif a == 2:
        ans1 = input(v1)
        ans3 = input(v3)
elif a == 3 :
    a = random.randint(1,2)
    ans3 = input(v3)
    if a == 1 :
        ans2 = input(v2)
        ans1 = input(v1)
    elif a == 2:
        ans1 = input(v1)
        ans2 = input(v2)
ans4 = input("Сколько милиардов лет земле ?(округлать в большую сторону)")
ans5 = input("Напишите нечего")
ans6 = input("Вам понравилась викторина")
print("Проверка ответов")
ansT = 0
if ans1.lower() == "семь":
    ansT += 1

if ans2.lower() == "солнце":
    ansT += 1    

if ans3 == "118":
    ansT += 1

if ans4 == "5":
    ansT += 1


if ans5 == "":
    ansT += 1

if ans6.lower() == "да":
    ansT += 1    
print (ansT,"из 6 ответов верно")
