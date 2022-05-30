# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c
"""
循環セールスマン問題

頂点Nで、重みが重みがC[i][j]の場合
・訪問ずみの頂点の組み合わせをbit表現する 
n:{}
例) 1100だと頂点3と2が訪問ずみ、1と0が未訪問
・集合nへ訪問ずみで、iへ訪問しようとする場合をDPで計算する
※ 訪問予定はj、現在位置はiとする
dp[n | 1 << j][j] = (dp[n][i] + DP[i][j]) or dp[n | 1 << j][j]

"""
N = int(input())
ALL = 1 << N
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)

dp = []
for _ in range(ALL):
    dp.append([10**18] * N)
dp[0][0] = 0

for n in range(ALL):
    for i in range(N):
        for j in range(N):
            # 同じ場所に留まることはできない
            if i == j:
                continue
            # 訪問ずみであればスキップ
            if n & (1 << j) > 0:
                continue
            dp[n | (1 << j)][j] = min(dp[n][i] + A[i][j], dp[n | (1 << j)][j])

print(dp[ALL - 1][0])
