def solution(money):
    def rob(nums):
        prev = 0
        curr = 0
        
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        
        return curr

    case1 = rob(money[:-1])
    
    case2 = rob(money[1:])
    
    return max(case1, case2)