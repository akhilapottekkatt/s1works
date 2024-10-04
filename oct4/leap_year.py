year=int(input("enter u want to find leapyears till the year"))
current_year=int(input("enter the current year"))
for i in range(current_year,year+1):
    
    if ((i%4==0 and i%100!=0) or (i%400==0)):
        print(f"{i} is leap year")

    else:
        print(f"{i}is no leap year")
