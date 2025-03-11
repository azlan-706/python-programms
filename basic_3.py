# Write a Python function that calculates the factorial of a given non-negative integer using recursion.
# by recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
ans=factorial(998)
print(ans)
print("-"*183)
# by for loop
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iterative(1558))  # Output: 120
