a=input("enter the word: ")
if len(a)%2!=0:
    mid=len(a)//2
    middle=a[mid]
else:
    mid=len(a)//2
    m=mid-1
    middle=a[m]+a[mid]
print(middle)    