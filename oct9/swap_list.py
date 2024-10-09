n=list(input("enter the values"))
print(n)
a=[]
c=n[len(n)-1]
a.append(c)
for x in n:
    print(x)
    b=n[0]
    if x!=b and x!=c:
        a.append(x)
a.append(b)
print(a)
    
    
