N = int(input())
scores = list(map(int, input().split()))

M = max(scores)

new_scores = []
for s in scores:
    new_scores.append(s / M * 100)

print(sum(new_scores) / N)