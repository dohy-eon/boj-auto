import heapq

def solution(n, k, enemy):
    heap = []
    
    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])
        n -= enemy[i]
        
        if n < 0:
            if k > 0:
                n += -heapq.heappop(heap)
                k -= 1
            else:
                return i
    
    return len(enemy)