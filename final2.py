a=int(input("enter the word you want to add: "))
i=1
list=[]
while(i<=a):
    word=input("word: ")
    i+=1
    list.append(word)
print(list)
print("output")
i=0
unique_words = []
while i<len(list):
    if list[i] in unique_words:
        i+=1
        continue
    u=list.count(list[i])
    print(u,end=" ")
    unique_words.append(list[i])
    i+=1
t=len(unique_words)
print()
print(t)