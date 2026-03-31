# 1 ~ N 큐에 넣기
# (K-1)번: 앞에서 빼서 뒤로 보내고
# K번째: popleft() 해서 제거하고 결과에 넣기
# 이걸 큐 빌 때까지

from collections import deque

N, K = map(int, input().split())

queue = deque(range(1, N + 1))
result = []

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")