from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]
queue = deque()

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append((i, j))
            dist[i][j] = 0

# BFS
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()