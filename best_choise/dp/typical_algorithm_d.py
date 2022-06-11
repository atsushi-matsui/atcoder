# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d
"""
ダイクトラム法
ヒープキューを利用して解く。
キューを取得する：O(logN)
キューを追加する：O(logN)
"""

import heapq

N, M = map(int, input().split())
G = []
for _ in range(M):
    G.append([])

for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))

# 距離
dist = [-1] * N
# 訪問済みであるのか
is_visited = [False] * N
# (距離、頂点)のキュー
Q = []
# 初期化
heapq.heappush(Q, (0, 0))
dist[0] = 0

while len(Q) > 0:
    d, s = heapq.heappop(Q)

    # ヒープキューでは始点からの総距離で昇順にソート済みで、訪問済みの頂点はすでに最短経路を算出済みのため、再計算の必要なし
    if is_visited[s]:
        continue
    is_visited[s] = True

    for g, c in G[s]:
        # 到達不可
        if c == 0:
            continue
        # 最小コストに更新
        if dist[g] == -1 or dist[g] > d + c:
            dist[g] = d + c
            heapq.heappush(Q, (dist[g], g))

print(dist[-1])
