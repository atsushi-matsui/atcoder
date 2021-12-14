# https://atcoder.jp/contests/abc068/tasks/arc079_a
# 幅優先探索

from collections import deque
# キュー
Q = deque()

N ,M = list(map(int, input().split()))
ship = []*N
dist = []
for _ in range(N):
    ship.append([]*N)
    dist.append(-1)
for _ in range(M):
    a, b =list(map(int, input().split()))
    ship[a-1].append(b-1)
    ship[b-1].append(a-1)

#初期値
Q.append(0)
dist[0] = 0

while len(Q) > 0:
    next = Q.popleft()
    for j in ship[next]:
        if dist[j] == -1:
            Q.append(j)
            dist[j] = dist[next] +1

#print(dist)

if dist[N-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")