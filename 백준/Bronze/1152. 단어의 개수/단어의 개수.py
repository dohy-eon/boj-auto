import sys

s = sys.stdin.readline().strip()

if s == "":
    print(0)
else:
    print(len(s.split()))