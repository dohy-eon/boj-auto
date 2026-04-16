from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(signals):
    periods = [g + y + r for g, y, r in signals]
    
    max_time = reduce(lcm, periods)
    
    for t in range(1, max_time + 1):
        ok = True
        
        for g, y, r in signals:
            cycle = g + y + r
            cur = (t-1) % cycle
            
            if not (g <= cur < g + y):
                ok = False
                break
        
        if ok:
            return t
    
    return -1