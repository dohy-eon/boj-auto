import sys
input = sys.stdin.readline

s = input().strip()

stack = []
result = []

priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

for ch in s:
    if ch.isalpha():
        result.append(ch)
    
    elif ch == '(':
        stack.append(ch)
    
    elif ch == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
    
    else:
        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[ch]:
            result.append(stack.pop())
        stack.append(ch)

while stack:
    result.append(stack.pop())

print(''.join(result))