import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

# DFS
visited_dfs = [False] * (n + 1)

def dfs(x):
    visited_dfs[x] = True
    print(x, end=' ')
    
    for next in graph[x]:
        if not visited_dfs[next]:
            dfs(next)

# BFS
def bfs(start):
    visited_bfs = [False] * (n + 1)
    queue = deque([start])
    visited_bfs[start] = True
    
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        
        for next in graph[now]:
            if not visited_bfs[next]:
                visited_bfs[next] = True
                queue.append(next)

dfs(v)
print()
bfs(v)