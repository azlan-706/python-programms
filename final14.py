s=input("enter the string: ")
def unique_in_order(s):
    count=1
    current_s=s[0]
    result=[]
    for i in range(1, len(s)):
            if s[i] == current_s:
                count += 1
            else:
                result.append(f" {current_s}")
                current_s = s[i]
                count = 1
    result.append(f"{current_s}")
    print(result)
unique_in_order(s)