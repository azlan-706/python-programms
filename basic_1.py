# Write a Python function that takes a list of numbers as input and returns their average. Handle empty lists by returning None.
def average(x):
    a=0
    if len(lis)!=0:
        for i in lis:
            a=a+i
        average=a//len(lis)
        print(average)
    else:
       print('none')
lis=[1,2,3,4,5]
average(lis)