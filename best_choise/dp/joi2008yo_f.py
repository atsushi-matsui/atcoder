# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
import heapq


def bfs(s, g, P):
    Q = []
    dist = [-1] * len(P)
    is_visited = [False] * len(P)

    # 初期化
    heapq.heappush(Q, (0, s))
    dist[s] = 0

    while len(Q) > 0:
        td, si = heapq.heappop(Q)

        if si == g:
            return td

        if is_visited[si]:
            continue

        is_visited[si] = True

        for gi, di in P[si]:
            if dist[gi] == -1 or dist[gi] > td + di:
                dist[gi] = td + di
                heapq.heappush(Q, (dist[gi], gi))


n, k = map(int, input().split())
GP = [] * n
for i in range(n):
    GP.append([])

res = []
for _ in range(k):
    line = list(map(int, input().split()))
    if line[0]:
        c = line[1] - 1
        d = line[2] - 1
        e = line[3]
        # ヒープキューでソーティングされるので航路が重複しても問題なし
        GP[c].append((d, e))
        GP[d].append((c, e))
    else:
        a = line[1] - 1
        b = line[2] - 1
        res.append(bfs(a, b, GP))

for r in res:
    if r is None:
        print(-1)
    else:
        print(r)
