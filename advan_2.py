# Write a Python function that sorts a list of strings based on their lengths. If two strings have the same length, sort them alphabetically.
def sorted_list(string):
    return sorted(string,key=lambda x:(len(x),x))
string=['apple','kiwi','grape','watermelon']
sort=sorted_list(string)
print(sort)