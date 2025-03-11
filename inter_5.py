# Write a Python function that takes two lists and returns a list of their common elements, sorted in ascending order.
def common(lis1,lis2):
    com=[]
    for value in lis1:
        if value in lis2 and value not in com:
            com.append(value)
    return sorted(com)
lis1=['k','h','a','l','i','d']
lis2=['a','z','l','a','n']
ans=common(lis1,lis2)
print(ans)