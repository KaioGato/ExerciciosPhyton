def evento(ag,d):
    (e,i,f) = ag
    if i>=1 and i<=366 and f>i and f<=366:
        if d>=i and d<=f : return e
        else : return 0
    else : return 0

def pontos(p1,p2):
    (a,b)=p1
    (c,d)=p2
    if (a+c)%5== 0 : return (a+c)
    elif (a+d)%5 == 0 : return (a+d)
    elif (b+c)%5 == 0 : return (b+c)
    elif (b+d)%5 == 0 : return (b+d)
    else : return 0    