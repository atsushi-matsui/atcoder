#https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f
#計算量：（N+M）*logM　プリム法

import heapq

N, M = list(map(int, input().split()))

C = []
for i in range(N):
    C.append([])

for _ in range(M):
    u, v, c = list(map(int, input().split()))
    C[u].append((c, v))
    C[v].append((c, u))

# 訪問済みか
visited = [False]*N
# 訪問回数
visited_count = 0
# キュー
Q = []
# コスト合計
sum_cost = 0

#初期化
visited[0] = True
visited_count = 1
for (c, v) in C[0]:
    heapq.heappush(Q, (c, v))

while visited_count < N:
    c, v = heapq.heappop(Q)
    # マーク済み
    if visited[v]:
        continue
    
    sum_cost += c
    visited[v] = True
    visited_count += 1

    for (cq, vq) in C[v]:
        if visited[vq]:
            continue
        heapq.heappush(Q, (cq, vq))

print(sum_cost)