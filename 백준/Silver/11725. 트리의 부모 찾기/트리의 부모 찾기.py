import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

adj = [[] for i in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# BFS
queue = deque([1])
parent[1] = -1  # 루트 표시

while queue:
    cur = queue.popleft()

    for nxt in adj[cur]:
        if parent[nxt] == 0:   # 아직 방문 안 함
            parent[nxt] = cur
            queue.append(nxt)

# 출력
for i in range(2, N + 1):
    print(parent[i])