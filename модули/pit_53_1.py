def a (u):
    v=[]
    for i in range (len(u)):
        a = u[i]
        if a >= 1 :
            v.append(1)
        elif a <= -1 :
            v.append(-1)
        else:
           v.append(0)
    return(v)
            
def b (u):
    v=[]
    for i in range (len(u)):
        a = u[i]
        d = a*a
        v.append(d)
    return(v)
                                 
