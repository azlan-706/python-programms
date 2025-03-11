n=int(input("enter the col: "))
m=int(input("enter the row: "))
array = [[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        layer=min(i,j,m-1-i,n-1-j)+1
        array[i][j]=layer
for row in array:
    print(row)