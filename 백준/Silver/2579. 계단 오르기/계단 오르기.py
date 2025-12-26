n = int(input())

# 점수 저장용 리스트 (계단 별)
score = [0] * (n + 1)

# 계단 점수 입력 받기
for i in range(1, n + 1):
    score[i] = int(input())

if n == 1:
    print(score[1])

elif n == 2:
    print(score[1] + score[2])

else:
    dp = [0] * (n + 1)

    # 초기값 설정
    dp[1] = score[1]
    dp[2] = score[1] + score[2]

    for i in range(3, n + 1):
        dp[i] = max(
            # 방법 1: i-2에서 바로 i로 점프
            dp[i-2] + score[i],

            # 방법 2: i-3 → i-1 → i
            dp[i-3] + score[i-1] + score[i]
        )

    print(dp[n])