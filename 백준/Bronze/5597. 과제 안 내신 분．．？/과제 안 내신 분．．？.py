submitted = [False] * 31

for _ in range(28):
    n = int(input())
    submitted[n] = True
    
for i in range(1, 31):
    if not submitted[i]:
        print(i)