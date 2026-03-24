from collections import Counter

word = input().upper()
count = Counter(word)

max_count = max(count.values())
result = [k for k, v in count.items() if v == max_count]

print(result[0] if len(result) == 1 else "?")