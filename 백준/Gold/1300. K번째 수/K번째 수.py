import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

left, right = 1, k
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in range(1, N + 1):
        cnt += min(N, mid // i)

    if cnt >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)