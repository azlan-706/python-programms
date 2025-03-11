str="McDonald's"
result=""
for i in str:
    if i.isupper():
        if result:
            result+=" "
    result+=i
print(result)
