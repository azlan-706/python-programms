# def is_balanced(expression):
#     stack = []
#     brackets = {')': '(', '}': '{', ']': '['}  # Matching pairs

#     for char in expression:
#         if char in brackets.values():  # If it's an opening bracket
#             stack.append(char)
#         elif char in brackets.keys():  # If it's a closing bracket
#             if not stack or stack.pop() != brackets[char]:
#                 return False  # Unbalanced if no matching opening bracket

#     return len(stack) == 0  # If stack is empty, brackets are balanced

# # Example usage
# expr1 = "{[()()]}"  # Balanced
# expr2 = "{[(])}"    # Not balanced

# print(is_balanced(expr1))  # Output: True
# print(is_balanced(expr2))  # Output: False
def reverse_string(s):
    stack = list(s)  # Using a list as a stack
    reversed_str = ""
    
    while stack:
        reversed_str += stack.pop()  # Pop from stack and append to result
    
    return reversed_str

# Example usage
input_str = "hello"
print(reverse_string(input_str))  # Output: "olleh"
