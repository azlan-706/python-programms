str=["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k=int(input("enter the k: "))
lis=[]
for i in range(len(str)-k+1):
    con=""
    for j in range(k):
        con+=str[i+j]
    lis.append(con)
print(lis)
long=""
for i in lis:
    if len(i) > len(long):
        long=i
print("the first longest string is:",long)