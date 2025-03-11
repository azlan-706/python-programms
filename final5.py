def re(a):
    li=["!","@","#","$","%","&","1","2","3","4","5","6","7","8","9","0"]
    i=0
    while i<len(li):
     x=li[i]
     a=a.replace(f"{x}","")
     i+=1
    return a
n=int(input("enter the number of rows: "))
m=int(input("enter the number of col: "))
grid = [input() for _ in range(n)]
def decode_grid(grid):
    decoded=""
    for column in range(m):
        col_str=""
        for row in range(n):
            col_str+=grid[row][column]
        for char in col_str:
            
            decoded += re(char)
    return decoded
output=decode_grid(grid)
print(output)