current = list(map(int, input().split()))
correct = [1, 1, 2, 2, 2, 8]

result = [c - cur for c, cur in zip(correct, current)]
print(*result)