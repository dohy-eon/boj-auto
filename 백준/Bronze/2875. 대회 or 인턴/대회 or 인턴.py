N, M, K = map(int, input().split())

team = min(N // 2, M)

while team > 0:
    if N + M - (team * 3) >= K:
        break
    team -= 1

print(team)