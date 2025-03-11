x=input("enter the string: ")
def rev(x):
    x=x+" "
    t=""
    reverse=""
    for i in x:
        if i!=" ":
            t=i+t
        else:
            reverse=reverse+" "+t
            t=""
    print(reverse)
rev(x)