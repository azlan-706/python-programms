# Write a Python program that reads a text file and prints the total number of words in the file.
def count_words(text):
    return len(text.strip().split())
with open("aa.txt",'r')as b:
    lines=b.readlines()
text = " ".join(line.strip() for line in lines)
total=count_words(text)
print(total)