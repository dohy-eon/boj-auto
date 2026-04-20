n, m = map(int, input().split())

passwords = {}

for _ in range(n):
    site, pw = input().split()
    passwords[site] = pw

for _ in range(m):
    site = input().strip()
    print(passwords[site])