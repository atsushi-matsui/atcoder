# https://atcoder.jp/contests/abc068/tasks/arc079_a
# ダイクトラム法
# 計算量 log(N)*(M+N)

import heapq

#ヒープ
Q = []
N ,M = list(map(int, input().split()))
ship = []
done = [False]*N

for _ in range(N):
    ship.append([])

for _ in range(M):
    a, b = list(map(int, input().split()))
    ship[a-1].append(b-1)
    ship[b-1].append(a-1)

dist = []
for _ in  range(N):
   dist.append(-1)

#初期値
heapq.heappush(Q, (0, 0))
dist[0] = 0

while len(Q) > 0:
    current_sdist, current_ship = heapq.heappop(Q)
    if done[current_ship]:
        continue
    done[current_ship] = True

    for next_ship in ship[current_ship]:
        # 辺の重みは定数
        x = 1
        if dist[next_ship] == -1 or dist[next_ship] > dist[current_ship] + x:
            dist[next_ship] = dist[current_ship] + x
            heapq.heappush(Q, (dist[next_ship], next_ship))

if dist[N-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
