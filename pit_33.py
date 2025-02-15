mat = [10,20,10,20,30,40,30,50]
for i in range(len(mat)):
    for k in range(len(mat)):
        print(i,k)
        if mat[i] == mat[k]:
            mat.remove(mat[k])
    
print(mat)
