# https://atcoder.jp/contests/abc068/tasks/arc079_a
"""
重み1の最短経路問題をBFSで解いてみる
"""
from collections import deque

N, M = map(int, input().split())

G = []
for _ in range(N):
    G.append([] * N)

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


dist = [-1] * N
dist[0] = 0

Q = deque()
Q.append(0)

while len(Q) > 0:
    s = Q.popleft()
    for g in G[s]:
        if dist[g] != -1:
            continue
        dist[g] = dist[s] + 1
        Q.append(g)

if dist[N - 1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
