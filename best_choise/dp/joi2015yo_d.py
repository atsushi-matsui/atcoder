# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d
"""
都市iにj日後に着いた時の疲労度をdp[i][j]とする
都市i-1 から 都市iに行くまでの疲労度をdc、日数は必ず1日
1.移動する場合
dp[i][j] = dp[i-1][j-1] + dc
2.移動しない場合
dp[i][j] = dp[i][j-1]
"""
N, M = map(int, input().split())
D = []
for _ in range(N):
    D.append(int(input()))
C = []
for _ in range(M):
    C.append(int(input()))

dp = [[10**18] * (M + 1) for _ in range(N + 1)]
# 初期値
for i in range(M + 1):
    dp[0][i] = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dc = D[i - 1] * C[j - 1]
        dp[i][j] = min(dp[i][j], dp[i][j - 1], dp[i - 1][j - 1] + dc)

print(min(dp[N]))
