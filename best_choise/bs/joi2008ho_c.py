# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
"""
4回投げる = 2本の矢を同時に投げるを2回行う、と解釈する
・1投目の得点の可能性
N^2
・2投目の得点で、M -（1投目）が最小になるような2投目の得点を求める
これはlog(N)で探索可能

従って、計算量は N^2*log(N)
"""
from bisect import bisect_right

N, M = map(int, input().split())
P = []
for _ in range(N):
    P.append(int(input()))

# 2頭投げる場合の得点
PP = set()
# 投げない場合
P.append(0)
for pi in P:
    for pj in P:
        if pi + pj > M:
            continue
        PP.add(pi + pj)
PP = list(PP)
PP.sort()


# 2分探索
S = 0
for p in PP:
    x = bisect_right(PP, M - p)
    S = max(S, p + PP[x - 1])
    """
    # 自作2分探索だとTLEになる。
    left = 0
    right = len(PP)
    while right - left > 1:
        center = (right + left) // 2
        if PP[center] < (M - p):
            # left = center  + 1
            left = center
        else:
            right = center

    # S = max(S, p + PP[left + 1])
    S = max(S, p + PP[left])
    """

print(S)
