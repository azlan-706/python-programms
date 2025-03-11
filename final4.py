s=input("enter the string: ")
count=1
current_s=s[0]
result=[]
for i in range(1, len(s)):
        if s[i] == current_s:
            count += 1
        else:
            result.append(f"({count}, {current_s})")
            current_s = s[i]
            count = 1
result.append(f"({count}, {current_s})")
output=" ".join(result)
print(output)