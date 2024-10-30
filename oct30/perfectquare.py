a=int(input("enter starting of 4 digit :"))
b=int(input("enter range"))
c=[]
for i in range(1,1000):
    for j in range (a,b+1):
        if (i*i==j):
            if j%2==0:
                c.append(j)
print("even and perfect squares")
print(c)
                
