N, M = map(int, input().split())
lectures = list(map(int, input().split()))

def can(mid):
    cnt = 1
    total = 0
    
    for x in lectures:
        if total + x > mid:
            cnt += 1
            total = x
        else:
            total += x
    
    return cnt <= M

left = max(lectures)
right = sum(lectures)

answer = right

while left <= right:
    mid = (left + right) // 2
    
    if can(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)