import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    p = int(input())
    
    if p == 0:
        stack.pop()
    else:
        stack.append(p)

print(sum(stack))