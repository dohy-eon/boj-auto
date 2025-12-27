arr = [False] * 42
for _ in range(10):
    arr[int(input()) % 42] = True
    
print(sum(arr))