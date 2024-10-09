
a,b,c=map(int, input("enter three num:").split())
print(a,b,c)
if a>b and a>c:
    print(a,"is greater in three")
elif(b>a) and (b>c):
    print(b,"is greater in three")

else:
    print(c,"is greter")

