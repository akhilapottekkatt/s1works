b=[]
count=0
size=int(input("enter size"))
for i in range(size):
    a=int(input("enter values"))
    b.append(a)

print("find the max value",max(b))
print("find the minimum value",min(b))
print("find the count of 1 in list",b.count(1))
print("find the sum of list",sum(b))

f=int(input("enter the number to count"))
for i in b:
    if ( i==f):
        count=count+1
print(count)
if count==0:
    print("the elemnet not in list")
    
