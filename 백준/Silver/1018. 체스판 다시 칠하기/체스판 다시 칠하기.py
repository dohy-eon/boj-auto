import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

answer = float('inf')

for i in range(n - 7):
    for j in range(m - 7):
        w_start = 0
        b_start = 0
        
        for x in range(8):
            for y in range(8):
                current = board[i + x][j + y]
                
                if (x + y) % 2 == 0:
                    if current != 'W':
                        w_start += 1
                    if current != 'B':
                        b_start += 1
                else:
                    if current != 'B':
                        w_start += 1
                    if current != 'W':
                        b_start += 1
        
        answer = min(answer, w_start, b_start)

print(answer)