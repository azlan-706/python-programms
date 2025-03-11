# Write a Python function to check if a given string is a palindrome (reads the same forwards and backwards). Ignore case and spaces.
def palindrome(s):
    s = s.replace(" ", "")
    reversed_s = "".join(reversed(s))
    print(reversed_s)  
    if reversed_s==s:
        print("the string is palindrome")
    else:
        print("string is not palindrome")
s = "race car"
palindrome(s)