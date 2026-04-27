import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    i = 1
    while data[i] != -1:
        next_node = data[i]
        dist = data[i + 1]
        graph[node].append((next_node, dist))
        i += 2

def dfs(start):
    visited = [-1] * (V + 1)
    visited[start] = 0
    
    stack = [start]
    
    while stack:
        cur = stack.pop()
        for nxt, cost in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + cost
                stack.append(nxt)
    
    max_dist = max(visited)
    max_node = visited.index(max_dist)
    
    return max_node, max_dist

far_node, _ = dfs(1)

_, diameter = dfs(far_node)

print(diameter)