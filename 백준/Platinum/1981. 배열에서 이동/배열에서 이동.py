from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(L, R):
    if not (L <= arr[0][0] <= R):
        return False
    
    visited = [[False]*n for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        
        if (x, y) == (n-1, n-1):
            return True
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and L <= arr[nx][ny] <= R:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
    return False


answer = 200
left = 0
right = 0

while left <= 200 and right <= 200:
    if bfs(left, right):
        answer = min(answer, right - left)
        left += 1
    else:
        right += 1

print(answer)