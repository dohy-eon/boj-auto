N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))
    
arr.sort()

for x in arr:
    print(x)