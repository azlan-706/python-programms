# Write a Python function that takes a list as input and returns a new list containing only the unique elements of the original list, preserving the order.
def unique(lis):
    uni=[]
    for item in lis:
        if item not in uni:
            uni.append(item)
    print(uni)
lis=["apple","banana","apple","car","toy","car"]
unique(lis)