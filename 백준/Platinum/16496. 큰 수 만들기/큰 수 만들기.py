n = int(input())
nums = list(input().split())

nums.sort(key=lambda x: x * 10, reverse=True)

result = ''.join(nums)

if result[0] == '0':
    print(0)
else:
    print(result)