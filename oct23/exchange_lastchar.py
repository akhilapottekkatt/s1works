a=input("enter the string")
b=[]
c=[]
for i in a:
    b.append(i)
print(b)
print(b[0])
print(b[-1])
c.append(b[-1])
for i in b:
    if i!=b[0] and i!=b[-1]:
        c.append(i)
c.append(b[0])
print(c)
        


    
    
