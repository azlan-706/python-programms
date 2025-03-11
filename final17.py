n=input("enter the number: ")
p=int(input("enter the power: "))
lis=[]
sum=0
for i in n:
    b=int(i)
    pp=b**p
    p+=1
    sum+=pp
a=int(n)
k=sum//a
if k>1:
    print(f"k = {k}")
else:
    print("k do not exists")
