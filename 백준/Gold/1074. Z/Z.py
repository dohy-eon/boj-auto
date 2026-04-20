import sys
input = sys.stdin.readline

def solve(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    
    # 1사분면
    if r < half and c < half:
        return solve(n-1, r, c)
    
    # 2사분면
    elif r < half and c >= half:
        return half * half + solve(n-1, r, c - half)
    
    # 3사분면
    elif r >= half and c < half:
        return 2 * half * half + solve(n-1, r - half, c)
    
    # 4사분면
    else:
        return 3 * half * half + solve(n-1, r - half, c - half)

n, r, c = map(int, input().split())
print(solve(n, r, c))