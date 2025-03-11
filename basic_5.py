# Write a Python function that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string (case-insensitive).
def vowel(str):
    lis=[]
    vl=['a','e','i','o','u']
    count=0
    for i in string:
        if i in vl:
            lis.append(i)
            count+=1      
    print(f"ther are {count} vowels in string")
    print(lis)    
string="my name is azlan khalid"
vowel(string)
