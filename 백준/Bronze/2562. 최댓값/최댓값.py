arr = []

for i in range(9):
    arr.append(int(input()))
    
max_value = max(arr)
index = arr.index(max_value) + 1

print(max_value)
print(index)