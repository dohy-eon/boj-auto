import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    line = input().strip()
    stack = []
    
    for char in line:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")