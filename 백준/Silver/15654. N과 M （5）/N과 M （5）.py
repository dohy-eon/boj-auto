N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

visited = [False] * N
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            
            dfs()
            
            result.pop()
            visited[i] = False

dfs()