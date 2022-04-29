# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
# 計算量：O(HWN)
from collections import deque

H, W, N = map(int, input().split())
C = []
for i in range(H):
    C.append(input())


def is_check(y, x, dist):
    # 範囲内であるか
    if 0 <= y < H and 0 <= x < W:
        # 通過ずみであるか
        if dist[y][x] != -1:
            return False
        # 障害物があるか
        if C[y][x] == "X":
            return False
        return True
    else:
        return False


def bfs(sy, sx, gy, gx):
    dist = []
    for _ in range(H):
        dist.append([-1] * W)

    # 障害物はX 、空き地である場合は .
    q = deque()
    # 初期値
    dist[sy][sx] = 0
    # 座標y ,座標x,残りの体力、食べたチーズの数
    q.append((sy, sx))

    while len(q) > 0:
        if dist[gy][gx] != -1:
            break

        y, x = q.popleft()

        for ty, tx in [[y, x - 1], [y - 1, x], [y, x + 1], [y + 1, x]]:
            if is_check(ty, tx, dist):
                dist[ty][tx] = dist[y][x] + 1
                q.append((ty, tx))

    return dist[gy][gx]


G = [()] * (N + 1)
for h in range(H):
    for w in range(W):
        if C[h][w] == "S":
            G[0] = (h, w)
        elif C[h][w] in str([1, 2, 3, 4, 5, 6, 7, 8, 9]):
            G[int(C[h][w])] = (h, w)

result = 0
for n in range(1, N + 1):
    sy, sx = G[n - 1]
    gy, gx = G[n]
    result += bfs(sy, sx, gy, gx)

print(result)
