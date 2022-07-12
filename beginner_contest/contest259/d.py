# https://atcoder.jp/contests/abc259/tasks/abc259_d
"""
無向辺のグラフへと帰着させてO(N**2)で解く。

1.円を頂点(xn, yn)の半径0とする
2.以下の公式から円同士が交差するか判定する
 ・内部に存在する事を
 (xi-xj)**2 + (yi-yj)**2  < (ri-rj)**2
 ・外部に存在する事を
 (xi-xj)**2 + (yi-yj)**2  > (ri+rj)**2
3.交差すれば無向辺をはる:O(N**2)
4.全探索で到達可能か検索する

Todo
- pypyじゃないとtimeoutする
"""
import sys

sys.setrecursionlimit(10**9)

N = int(input())
sx, sy, tx, ty = map(int, input().split())
C = []
for _ in range(N):
    x, y, r = map(int, input().split())
    C.append((x, y, r))
# 無効辺
V = []
for _ in range(N):
    V.append([] * N)

# 無向辺のグラフを作成
for i, ci in enumerate(C):
    xi = ci[0]
    yi = ci[1]
    ri = ci[2]
    for j, cj in enumerate(C):
        xj = cj[0]
        yj = cj[1]
        rj = cj[2]
        if (xi - xj) ** 2 + (yi - yj) ** 2 < (ri - rj) ** 2:
            continue
        if (xi - xj) ** 2 + (yi - yj) ** 2 > (ri + rj) ** 2:
            continue
        V[i].append(j)
        V[j].append(i)

S = []
T = []
# 始点が含まれる円
for i, ci in enumerate(C):
    xi = ci[0]
    yi = ci[1]
    ri = ci[2]
    if (xi - sx) ** 2 + (yi - sy) ** 2 == ri**2:
        S.append(i)
    if (xi - tx) ** 2 + (yi - ty) ** 2 == ri**2:
        T.append(i)


def dfs(i, visited):
    if visited[i]:
        return
    visited[i] = True

    for v in V[i]:
        dfs(v, visited)


res = False
for s in S:
    visited = [False] * N
    dfs(s, visited)
    for t in T:
        if visited[t]:
            res = True
            break
    if res:
        break

if res:
    print("Yes")
else:
    print("No")
