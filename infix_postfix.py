class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None
    def isEmpty(self):
        return len(self.stack) == 0
# Function to get precedence of operators
def precedence(char):
    if char == '^':
        return 3
    elif char in ('/', '*'):
        return 2
    elif char in ('+', '-'):
        return 1
    else:
        return 0
# Function to check if character is an operand
def isOperand(char):
    return char.isalnum()  # Checks if alphanumeric (a-z, A-Z, 0-9)
# Function to convert infix to postfix
def infixToPostfix(s, st):
    postFix = []
    for i in range(len(s)):
        if isOperand(s[i]):
            postFix.append(s[i])
            
        elif s[i] == '(':
            st.push(s[i])
        elif s[i] == ')':
            while not st.isEmpty() and st.peek() != '(':
                postFix.append(st.pop())  # Pop operators
            st.pop()  # Pop '('
        else:
            while (not st.isEmpty()) and (precedence(s[i]) <= precedence(st.peek())):
                postFix.append(st.pop())  # Pop higher precedence operators
            st.push(s[i])
    while not st.isEmpty():
        postFix.append(st.pop())  # Pop remaining operators
    return ''.join(postFix)  # Convert list to string
# Example Usage
expression = "a+b*(c^d-e)^(f+g*h)-i"
st = Stack()
print(infixToPostfix(expression, st))  # Output: abcd^e-fgh*+^*+i-
