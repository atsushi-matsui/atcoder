# https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_e

from collections import deque
import heapq
from re import I

N, K = map(int, input().split())
C = []
R = []
for _ in range(N):
    c, r = map(int, input().split())
    C.append(c)
    R.append(r)

P = []
for _ in range(N):
    P.append(set())

for _ in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    P[a].add(b)
    P[b].add(a)


# 1. グラフPには距離の制約があるので、距離を1としたグラフVを生成する
V = []
for _ in range(N):
    # NOTICE: setにするとMLEになったので、pypyでやるならlistにすること
    V.append([])
    
for i in range(N):
    qq = deque()
    qq.append((i, 0))
    is_visited = [False] * N
    is_visited[i] = True
    while len(qq) > 0:
        s, d = qq.popleft()
        if d >= R[i]:
            continue
        
        for p in P[s]:
            if not is_visited[p]:
                qq.append((p, d + 1))
                V[i].append(p)
                is_visited[p] = True

# 2. グラフVからダイクトラム法で作成する

# NOTICE: tupleをheapQueueに入れると遅いようなのでintで扱うで扱う → 効果なし
"""
def pack(cost, t, k):
    return cost*k + t
def unpack(v,k):
    return(v//k, v%k)
"""
    

is_visited = [False] * N
TC = [-1] * N
Q = []
heapq.heappush(Q, [0, 0])


while len(Q) > 0:
    c, n = heapq.heappop(Q)

    if is_visited[n]:
        continue
    is_visited[n] = True

    for v in V[n]:
        if TC[v] == -1 or TC[v] > C[n] + c:
            TC[v] = C[n] + c
            heapq.heappush(Q, [TC[v], v])

print(TC[-1])
