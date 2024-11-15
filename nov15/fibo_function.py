def fibo(d):
    a=0
    b=1
    c=0
    e=[]
    for i in range (d):
        if (i==0 or i==1):
            e.append(i)
        else:
            c=a+b
            e.append(c)
            a=b
            b=c
    print(e)
