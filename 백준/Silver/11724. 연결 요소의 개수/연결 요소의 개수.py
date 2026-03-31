# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# 방문 안한 노드에서 DFS 시작 할 때마다 +1
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 그래프 만들기 끝

visited = [False] * (n+1)

def dfs(x):
    visited[x] = True

    for next in graph[x]:
        if not visited[next]:
            dfs(next) # dfs 함수

count = 0

for i in range(1, n+1): # 전체 노드 검사
    if not visited[i]: # 새로운 덩어리(노드) 발견 시
        dfs(i) # 해당 노드들 싹 돌기
        count += 1

print(count)