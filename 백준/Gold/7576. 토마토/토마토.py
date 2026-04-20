import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < N and 0 <= ny < M:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

answer = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        answer = max(answer, box[i][j])

print(answer - 1)