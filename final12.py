str="4of Fo1r pe6ople g3ood th5e the2"
lis=str.split(" ")
lis2=[]
pair=[]
for i in lis:
    for char in i:
        if char.isdigit():
            lis2.append(int(char))
            pair.append((char,i))
pair.sort()
result = ' '.join(word for _, word in pair)
print(result)