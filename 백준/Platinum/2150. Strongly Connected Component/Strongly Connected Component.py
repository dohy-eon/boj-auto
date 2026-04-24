import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)

id = 0
d = [0] * (V + 1)
low = [0] * (V + 1)
finished = [False] * (V + 1)
stack = []

SCC = []

def dfs(x):
    global id
    id += 1
    d[x] = low[x] = id
    stack.append(x)

    for nxt in graph[x]:
        if d[nxt] == 0:
            dfs(nxt)
            low[x] = min(low[x], low[nxt])
        elif not finished[nxt]:
            low[x] = min(low[x], d[nxt])

    if d[x] == low[x]:
        scc = []
        while True:
            t = stack.pop()
            finished[t] = True
            scc.append(t)
            if t == x:
                break
        scc.sort()
        SCC.append(scc)

for i in range(1, V + 1):
    if d[i] == 0:
        dfs(i)

SCC.sort(key=lambda x: x[0])

print(len(SCC))
for scc in SCC:
    print(*scc, -1)