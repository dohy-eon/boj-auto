import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

count = {}

for c in cards:
    count[c] = count.get(c, 0) + 1

for t in targets:
    print(count.get(t, 0), end=' ')