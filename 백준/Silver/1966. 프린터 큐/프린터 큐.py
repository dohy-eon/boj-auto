from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    
    q = deque([(importance[i], i) for i in range(n)])
    
    count = 0
    
    while q:
        cur = q.popleft()
        
        # if 더 높은 중요도가 존재하면 뒤로
        if any(cur[0] < x[0] for x in q):
            q.append(cur)
        else:
            count += 1
            
            if cur[1] == m:
                print(count)
                break