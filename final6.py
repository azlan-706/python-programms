list=[1,4,7,-12]
i=0
while i<=len(list):
    while i<len(list) and list[i]<0:
        list.remove(list[i])
    i+=1
print(list)
print(sum(list))