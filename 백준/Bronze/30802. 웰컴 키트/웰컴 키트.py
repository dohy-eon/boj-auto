n = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠
tshirt = 0
for s in sizes:
    tshirt += (s + T - 1) // T

print(tshirt)

# 펜
print(n // P, n % P)