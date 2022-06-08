# https://atcoder.jp/contests/s8pc-1/tasks/s8pc_1_g
N, M = map(int, input().split())
ST = []
DT = []
INF = 10**18
for _ in range(N):
    DT.append([(0, 0)] * N)
for _ in range(M):
    s, t, d, time = map(int, input().split())
    s -= 1
    t -= 1
    ST.append((s, t))
    ST.append((t, s))
    DT[s][t] = (d, time)
    DT[t][s] = (d, time)

dp = []
count = []
for i in range(1 << N):
    dp.append([INF] * N)
    count.append([0] * N)
# 開始点は必ず建物1から
dp[0][0] = 0
count[0][0] = 1

# pypy3じゃないとTLEになるのでメモ化再起のパターンもやってみる
for i in range(1 << N):
    for s, t in ST:
        d, time = DT[s][t]
        # 行き先が訪問済みであればスキップ
        if i != 0 and (i >> t) & 1 != 0:
            continue
        # 制限外であればスキップ
        if dp[i][s] + d > time:
            continue

        if dp[i | 1 << t][t] > dp[i][s] + d:
            dp[i | 1 << t][t] = dp[i][s] + d
            count[i | 1 << t][t] = count[i][s]
        elif dp[i | 1 << t][t] == dp[i][s] + d:
            count[i | 1 << t][t] += count[i][s]

# print(dp[-1])
# print(count[-1])

if dp[-1][0] == INF:
    print("IMPOSSIBLE")
else:
    print(dp[-1][0], count[-1][0])

"""
N, M = map(int, input().split())
ST = []
DT = []
S = set()
for _ in range(N + 1):
    DT.append([(0, 0)] * (N + 1))
for _ in range(M):
    s, t, d, time = map(int, input().split())
    s -= 1
    t -= 1
    S.add(s)
    ST.append((s, t))
    ST.append((t, s))
    DT[s][t] = (d, time)
    DT[t][s] = (d, time)
S = list(S)

INF = 10**18
dp = []
for _ in range(1 << N):
    dp.append([-1] * N)


def dfs(bit, v, dist):
    # 訪問済みであればメモを返す
    if dp[bit][v] != -1:
        return (dp[bit][v], 0)

    # 全ての頂点を訪れて頂点に戻ってきた
    if bit == (1 << N) - 1 and v == start:
        # print(f"#1 bit={bin(bit)}, v={v}")
        return (0, 1)
    elif bit == (1 << N) - 1 and v != start:
        # print(f"#2 bit={bin(bit)}, v={v}")
        return (INF, 0)

    res = INF
    count = 0
    for s, t in ST:
        if s != v or (bit >> t & 1) != 0:
            continue
        d, time = DT[s][t]
        # print(f"bit={bin(bit)}, v={v}")
        # print(f"s={s}, t={t}, d={d}, time={time}, dp={dp[bit][v]}, dist={dist}")
        # 通行可能
        if dist < time:
            r, c = dfs(bit | 1 << t, t, dist + d)
            # print(f"r={r}, c={c}")
            if res > r + d:
                # print(f"r={r}, count={count}")
                res = r + d
                # dp[bit][v] = res
                count = c
            elif res == r + d:
                count += c
                # print(f"r={r}, count={count}")
        # 通行不可
        else:
            pass
            # return (INF, 0)
    dp[bit][v] = res

    return (res, count)


start = S[0]
ans = dfs(0, start, 0)
if ans[0] == INF:
    print("IMPOSSIBLE")
else:
    print(ans[0], ans[1])
"""
