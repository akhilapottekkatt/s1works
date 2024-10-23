a=[]
b=[]
Sum=[]

s1=int(input("enter the size"))
s2=int(input("enter the size of second array"))
for i in range(0,s1):
    c=int(input("enter the elements"))
    a.append(c)
print("first array",a)

for i in range(0,s2):
    d=int(input("enter the values"))
    b.append(d)
print("second array",b)
print("check the length\n" )
print("length of first array",len(a))
print("lenth of second array",len(b))
if(len(a)==len(b)):
    print("equal enegth of lists")
for i in a:
    for j in b:
        if i==j:
            print(i,"in both list")
            Sum.append(i+j)
print(Sum)
            
        
    
    
    
