import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

def dfs(x, y, depth, total):
    global answer

    if depth == 4:
        answer = max(answer, total)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

def check_t(x, y):
    global answer
    tmp = []

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            tmp.append(board[nx][ny])

    if len(tmp) >= 3:
        tmp.sort(reverse=True)
        answer = max(answer, board[x][y] + tmp[0] + tmp[1] + tmp[2])

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

        check_t(i, j)

print(answer)