import sys
input = sys.stdin.readline

line_num = int(input())
stack = []
current = 1
result = []

for _ in range(line_num):
    num = int(input())

    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    
    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit()

print('\n'.join(result))