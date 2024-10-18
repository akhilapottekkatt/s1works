a=[]
count=0
size=int(input("size of list"));
for i in range(0,size):
        b=input("enter the first name");
        a.append(b)
print(a)
for i in a:
    print(i.split())
    for j in i:
        print(j)
        if j=="a" or j=="A":
            count=count+1
print("total numb of a in list is",count)
    
