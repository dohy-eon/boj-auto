S = input().strip()

pos = [-1] * 26

for i in range(len(S)):
    idx = ord(S[i]) - ord('a')
    if pos[idx] == -1:
        pos[idx] = i

print(*pos)
