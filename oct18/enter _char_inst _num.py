a=[]
size=int(input("size of list"));
for i in range(0,size):
        b=int(input("enter the values"));
        if b<=100:
            a.append(b)

        else:
            a.append("over")

print(a)
        
