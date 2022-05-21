# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
"""
選択なし :0
トマトソース :1
クリームソース :2
バジルソース :3

f(i+1, A, B) = f(i, A', B')
"""

N, K = map(int, input().split())
AB = {}
for _ in range(K):
    a, b = map(int, input().split())
    AB.update({a: b})

# FIXME 3重配列の作成方法
DP = [[[0] * 4 for i in range(4)] for j in range(N + 1)]

"""
0日目 DP[0][0][0] にだけ初期値1を与える
1日目 DP[1][1 ~ 3][0]
2日目以降 DP[2~][1 ~ 3][0 ~ 3 で値は入るが、1日目の結果でi=0の場合は必ず0であるため実質は 1 ~ 3]
"""
# 0日目に1つだけ初期値を入れる
DP[0][0][1] = 1
# 2日前がj、1日前がi、現在がkのタイミングでパスタを食べる
for n in range(N):
    b = AB.get(n + 1)
    # kのrangeは1~3なのでiとjで0~3の範囲でloopしても問題ない
    for i in range(4):
        for j in range(4):
            for k in range(1, 4):
                # k日目に食べるパスタと異なる場合はスキップ
                if b is not None and b != k:
                    continue
                # 2日以降で選択なしの場合はスキップ
                if n >= 2 and (i == 0 or j == 0):
                    continue
                # 3日連続の場合もスキップ
                if k == i == j:
                    continue
                DP[n + 1][k][i] += DP[n][i][j]

result = 0
for i in range(1, 4):
    for j in range(1, 4):
        result += DP[-1][i][j]

print(result % 10000)
