f1 = open('data.txt')
b = f1.read()
b = b.replace ("one","один")
b = b.replace ("two","два")
b = b.replace ("three","три")
b = b.replace ("four","четыре")
b = b.replace ("five","пять")
f2 = open('data2.txt','x')
f2.write(b)
f2.close()
f1.close()
