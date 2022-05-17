# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d
"""
動的計画法
i:数字を選んだ数
j:1~20の数値
DP[i][j]:選択肢の数

1.プラスの場合
DP[i][j] = 現在の選択肢数 + 1つ前の(j-k) が持つ選択肢数
2.マイナスの場合
DP[i][j] = 現在の選択肢数 + 1つ前の(j+k) が持つ選択肢数

"""

N = int(input())
L = list(map(int, input().split()))

DP = []
for l in range(len(L)):
    DP.append([0] * 21)
# 初期値
DP[0][L[0]] = 1

for i in range(1, len(L) - 1):
    for j in range(21):
        # プラスの場合
        if 0 <= j - L[i] <= 20:
            if DP[i - 1][j - L[i]] > 0:
                DP[i][j] += DP[i - 1][j - L[i]]
        # マイナスの場合
        if 0 <= j + L[i] <= 20:
            if DP[i - 1][j + L[i]] > 0:
                DP[i][j] += DP[i - 1][j + L[i]]

# 最後
i = len(L) - 1
for j in range(21):
    # マイナスの場合
    if 0 <= j + L[i] <= 20:
        if DP[i - 1][j + L[i]] > 0:
            DP[i][j] += DP[i - 1][j + L[i]]

print(DP[len(L) - 1][0])
