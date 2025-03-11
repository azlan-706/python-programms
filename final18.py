str=input("enter: ")
count=0
if str[0]=="(":
    for i in str:
        if i=="(":
            count+=1
        if i==")":
            count-=1
    if count==0:
        print(f"{str} is valid")
    else:
        print(f"{str} is not valid")
else:
    print(f"{str} is not valid")