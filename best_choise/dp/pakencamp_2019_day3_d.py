"""
i列をj色にした時の変更数
dp[i][j]
i列をj色に変えた場合の最小
dp[i][j] = dp[i-1][W] or dp[i-1][R] or dp[i-1][B]
"""

N = int(input())
S = []
for _ in range(5):
    S.append(list(input()))

dp = [[10**18] * 3 for _ in range(N)]

# 初期値を代入
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0
for i in range(5):
    if S[i][0] != "R":
        dp[0][0] += 1
    if S[i][0] != "B":
        dp[0][1] += 1
    if S[i][0] != "W":
        dp[0][2] += 1
# start
for i in range(1, N):
    for j in range(3):
        count = 0
        if j == 0:
            color = "R"
        elif j == 1:
            color = "B"
        elif j == 2:
            color = "W"
        for l in range(5):
            if color != S[l][i]:
                count += 1
        for k in range(3):
            # 同色の場合はスキップ
            if j == k:
                continue
            dp[i][j] = min(dp[i][j], dp[i - 1][k])
        dp[i][j] += count
        # print(dp)

print(min(dp[N - 1]))
