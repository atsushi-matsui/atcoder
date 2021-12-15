# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d
# ダイクトラム法
# 計算量 log(N)*(M+N)

import heapq

N, M = list(map(int, input().split()))
geografy = []

for _ in range(N):
    geografy.append([])

for _ in range(M):
    u, v, c = list(map(int, input().split()))
    geografy[u].append([v ,c])
  
Q = []
dist = [-1]*N
done = [False]*N

heapq.heappush(Q, (0, 0))
dist[0] = 0

while len(Q) > 0:
    cost, position = heapq.heappop(Q)
    if done[position]:
        continue
    done[position] = True

    for g in geografy[position]:
        v = g[0]
        c = g[1]
        if dist[v] == -1 or dist[v] > (dist[position] + c):
            dist[v] = dist[position] + c
            heapq.heappush(Q, (dist[v], v))

print(dist[N-1])