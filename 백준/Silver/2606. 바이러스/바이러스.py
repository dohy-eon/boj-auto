import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(x):
    visited[x] = True
    count = 1

    for next in graph[x]:
        if not visited[next]:
            count += dfs(next)
        
    return count

print(dfs(1) - 1)