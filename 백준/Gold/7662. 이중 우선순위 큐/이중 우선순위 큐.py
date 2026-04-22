import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    
    min_h = []
    max_h = []
    visited = [False] * k
    
    for i in range(k):
        cmd, n = input().split()
        n = int(n)
        
        if cmd == 'I':
            heapq.heappush(min_h, (n, i))
            heapq.heappush(max_h, (-n, i))
            visited[i] = True
        
        else:
            if n == 1:
                # 최대값 삭제
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)
            
            else:
                # 최소값 삭제
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)
    
    # 마지막 정리 (cleanup)
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
    
    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(-max_h[0][0], min_h[0][0])