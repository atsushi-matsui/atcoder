# https://atcoder.jp/contests/abc138/tasks/abc138_d
import sys

sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
node = [] * N
for _ in range(N):
    node.append([])

for _ in range(N - 1):
    a, b = map(int, input().split())
    # 無向グラフなので両辺を追加
    node[b - 1].append(a - 1)
    node[a - 1].append(b - 1)


points = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    points[p - 1] += x


result = [0] * N


def dp(c, p):
    if c > (N - 1):
        return
    for n in node[c]:
        # 1つ前の頂点と現在のノードが一致しているなら探索済みとする
        if n != p:
            points[n] += points[c]
            dp(n, c)


dp(0, -1)

arr = [str(i) for i in points]
print(" ".join(arr))
