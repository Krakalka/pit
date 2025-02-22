d=0
while d == 0:
    a = input("")
    print("Rekomendovano :", end=" ")
    try:
        a = float(a)
        d = 1
    except:
        print("try again")
    else:
        if 3 <= a <6:
            print("поесть")
        elif 6 <= a <12:
            print("пережить первую часть школы")
        elif 12 <= a <16:
            print("пережить первую часть школы")
        elif 16 <= a:
            print("купить машину")
        else:
            print("выжить")
