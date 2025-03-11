import time
def random(x,y):
    # LCG Parameters
    a = 1664525
    c = 1013904223
    m = 2**32
    # Use the current time in microseconds as a default seed
    seed = int(time.time() * 1000000) % m
    # Generate the random number
    seed = (a * seed + c) % m
    # Scale the random number to the desired range [start, end]
    random_in_range = x + (seed % (y - x + 1))
    return random_in_range
# # Get input from user
x = int(input("Enter the start of the range: "))
y = int(input("Enter the end of the range: "))
# # Generate random numbers
print(random(x, y))
# def from_list(lis):
#     l=len(lis)-1
#     i=random(0,l)
#     print(lis[i])
# lis=[x for x in range(1000,10000)]
# from_list(lis)