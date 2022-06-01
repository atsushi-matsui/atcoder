# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=ja
"""
1.全経路を通るの0スタート & ゴールと考える。
2.forループだとマニア間に合わないのでメモ化再帰を利用する。
"""
INF = 10**18

V, E = map(int, input().split())
ALL = 1 << V
D = []
for _ in range(V):
    D.append([INF] * V)

ST = []
for _ in range(E):
    s, t, d = map(int, input().split())
    ST.append((s, t))
    D[s][t] = d

dp = []

for _ in range(ALL):
    dp.append([-1] * V)


def dfs(bit_s, v):
    # 訪問ずみはメモを返す
    if dp[bit_s][v] != -1:
        return dp[bit_s][v]

    # 全ての頂点を訪れて頂点0に戻ってきた
    if bit_s == (1 << V) - 1 and v == 0:
        return 0

    res = INF
    for s, t in ST:
        if s == v and (bit_s >> t & 1) == 0:
            res = min(
                res,
                dfs(bit_s | 1 << t, t) + D[v][t],
            )
    dp[bit_s][v] = res
    return res


ans = dfs(0, 0)
if ans == INF:
    print(-1)
else:
    print(ans)

"""
# 初期値
dp[0][0] = 0

# これだとTLE
for i in range(ALL):
    for s, t in ST:
        # 訪問ずみはスキップ
        if D[s][t] == -1 or i & (1 << t) > 0:
            continue
        dp[i | 1 << t][t] = min(dp[i][s] + D[s][t], dp[i | 1 << t][t])

# 0に戻るのが結果
result = dp[ALL - 1][0]
if result == INF:
    print(-1)
else:
    print(result)
"""
