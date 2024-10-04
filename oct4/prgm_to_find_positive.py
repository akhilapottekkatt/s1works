new_lst=[]
lst=[-2,6,4,7,0,-3,-7]
for i in lst:
    if i>=0:
            print(f"{i} is positive")
            new_lst.append(i)
            
        
    else:
    
        print("not a positive number")
print(new_lst)
