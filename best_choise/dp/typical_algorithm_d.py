# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d
import heapq

N, M = map(int, input().split())
D = []
for _ in range(N):
    D.append([])
for _ in range(M):
    u, v, c = map(int, input().split())
    D[u].append((c, v))
# iまで到達するための最短コスト
C = [10**18] * N
# 訪問済みか
visited = [False] * N

# キュー
Q = []
heapq.heappush(Q, (0, 0))

while len(Q) > 0:
    c, s = heapq.heappop(Q)

    # コストのソート順に取得しているので、一度取り出したことのあるノードで再計算は不要
    if visited[s]:
        continue
    visited[s] = True

    for d, g in D[s]:
        if C[g] > c + d:
            C[g] = c + d
            heapq.heappush(Q, (C[g], g))

print(C[N - 1])
