# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja
"""
同じ品物であれば何度も選べるというのがポイント
#  https://prdc.hatenablog.com/entry/2017/09/12/140232
●考え方
v:価値, w:重さ
1.品物を選んだ場合
    dp[i-1][j-w] + w
2.品物を選ばなかった場合
    dp[i-1][j]
3.同じ品物を選ぶ場合
    dp[i][j-w]

"""
N, W = map(int, input().split())
VW = []
for _ in range(N):
    VW.append(list(map(int, input().split())))


Value = []
for _ in range(N):
    Value.append([0] * (W + 1))

# 初期値
sv, sw = VW[0]
for j in range(W + 1):
    if j % sw == 0:
        Value[0][j] = sv * (j // sw)

# DP
for i in range(1, N):
    for j in range(W + 1):
        v, w = VW[i]
        Value[i][j] = max(Value[i][j], Value[i - 1][j])
        if j - w >= 0:
            Value[i][j] = max(Value[i][j], Value[i - 1][j - w] + v, Value[i][j - w] + v)

print(max(Value[N - 1]))
