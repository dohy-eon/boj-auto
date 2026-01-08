# 완전회문 -> 0 | 거의 회문 -> 1 | 회문x -> 2
# 투포인터 사용

import sys
input = sys.stdin.readline

def is_pal(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

T = int(input())

for _ in range(T):
    s = input().strip()
    l, r = 0, len(s) - 1
    result = 0

    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            # 한 글자 삭제
            if is_pal(s, l + 1, r) or is_pal(s, l, r - 1):
                result = 1
            else:
                result = 2
            break

    print(result)