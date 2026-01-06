T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    
    result = ""
    for ch in S:
        result += ch * R
    
    print(result)
