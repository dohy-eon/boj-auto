# 인덱스 기준으로 하나씩
# 현재까지의 합을 계속 저장
# 타겟 도달 시에 출력

def solution(numbers, target):
    answer = 0
    
    def dfs(idx, total):
        nonlocal answer
        
        # 끝까지 다 썼을 때
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        
        # + 선택
        dfs(idx + 1, total + numbers[idx])
        
        # - 선택
        dfs(idx + 1, total - numbers[idx])
    
    dfs(0, 0)
    
    return answer