def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    
    both = lost & reserve
    lost -= both
    reserve -= both
    
    lost = sorted(lost)
    
    for student in lost:
        if student - 1 in reserve:
            reserve.remove(student - 1)
        elif student + 1 in reserve:
            reserve.remove(student + 1)
        else:
            n -= 1
    
    return n