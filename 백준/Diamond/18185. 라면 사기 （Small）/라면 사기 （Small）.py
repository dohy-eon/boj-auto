# 1개: 3원
# 2개: 5원 → 개당 2.5원
# 3개: 7원 → 개당 2.33원
# but if A[i+1] > A[i+2] 2개 묶음 먼저

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A += [0, 0]  # 범위 처리용

cost = 0

for i in range(n):
    # 2개 먼저
    if A[i+1] > A[i+2]:
        two = min(A[i], A[i+1] - A[i+2])
        cost += 5 * two
        A[i] -= two
        A[i+1] -= two

    # 3개
    three = min(A[i], A[i+1], A[i+2])
    cost += 7 * three
    A[i] -= three
    A[i+1] -= three
    A[i+2] -= three

    # 2개
    two = min(A[i], A[i+1])
    cost += 5 * two
    A[i] -= two
    A[i+1] -= two

    # 1개
    cost += 3 * A[i]
    A[i] = 0

print(cost)