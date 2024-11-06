dict1={}
tt=int(input("enter the total mark"))
dict1["name"]="akhila"
dict1["roll no"]=30
dict1["reg"]=18901
dict1["semester"]="s1"
print(dict1)
dict1["total mark"]=tt

if tt>=90:
    dict1["Grade"]="A"
elif tt>=82 and tt<=89:
    dict1["Grade"]="B"

elif tt>=75 and tt<=81:
    dict1["Grade"]="C"
elif tt>=60 and tt<=74:
    dict1["Grade"]="D"
elif tt>=50 and tt<=59:
    dict1["Grade"]="PASS"
else:
    dict1["Grade"]="FAIL"

print(dict1)
