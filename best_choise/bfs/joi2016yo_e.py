# https://atcoder.jp/contests/joi2016yo/tasks/joi2016yo_e
"""
ダイクストラ法（重みつきBFS）
O(log(N)*(M+N))

公式解説
https://www.ioi-jp.org/joi/2015/2016-yo/2016-yo-t5/review/2016-yo-t5-review.html
"""
from collections import deque
import heapq

N, M, K, S = map(int, input().split())
low, high = map(int, input().split())

# ゾンビがいる島と仮想の島N+1を結ぶ
ZG = []
# ゾンビのいる島
zombies = []
for _ in range(N + 1):
    ZG.append([])
for _ in range(K):
    z = int(input()) - 1
    zombies.append(z)
    ZG[N].append(z)

# 辺
G = []
for _ in range(N):
    G.append([])
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    ZG[a].append(b)
    ZG[b].append(a)
# コスト
C = [low] * N
TC = [-1] * N

"""
愚直にゾンビがいる島々から距離Kの島をそれぞれBFSで求めると、
TLEになるので仮想の島N+1からゾンビ島をそれぞれ繋いで、仮想の島から距離K+1までを求めるBFSを行う
"""
ZQ = deque()
ZQ.append((N, 0))
# ゾンビがいる島のコストは到達不可として-1にする
for z in zombies:
    C[z] = -1
is_zombie = [False] * (N + 1)
while len(ZQ) > 0:
    zq, d = ZQ.popleft()

    if is_zombie[zq]:
        continue
    is_zombie[zq] = True

    if d > S:
        continue

    for z in ZG[zq]:
        if C[z] == -1:
            ZQ.append((z, d + 1))
        else:
            C[z] = high
            ZQ.append((z, d + 1))


# 訪問済み
is_visited = [False] * N
# キュー
Q = []
# 初期化
heapq.heappush(Q, (0, 0))
# ダイクストラ法で求める
while len(Q) > 0:
    c, n = heapq.heappop(Q)
    # 訪問済みならば終了
    if is_visited[n]:
        continue
    is_visited[n] = True

    for g in G[n]:
        # ゾンビがいる島はいけない
        if C[g] == -1:
            continue
        if TC[g] == -1 or TC[g] > c + C[g]:
            TC[g] = c + C[g]
            heapq.heappush(Q, (TC[g], g))

# 最後の島では宿泊費がかからない
print(TC[N - 1] - C[N - 1])
