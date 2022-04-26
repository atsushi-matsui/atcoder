# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = []

for _ in range(R):
    c.append(input())

# 訪問済みか
is_visited = []
# スタートからの距離
dist = []
for _ in range(R):
    is_visited.append([False] * C)
    dist.append([0] * C)

# キュー
q = deque()


def is_check(y, x):
    if 0 <= y < R and 0 <= x < C:
        # 訪問ずみ
        if is_visited[y][x]:
            return False
        # 壁なら進めない
        if c[y][x] == "#":
            return False

        is_visited[y][x] = True
        return True

    return False


q.append((sy - 1, sx - 1))
while len(q) > 0:
    ty, tx = q.popleft()
    if ty == gy - 1 and tx == gx - 1:
        break

    for i, j in [[ty, tx - 1], [ty - 1, tx], [ty, tx + 1], [ty + 1, tx]]:
        if is_check(i, j):
            dist[i][j] = dist[ty][tx] + 1
            q.append((i, j))

print(dist[gy - 1][gx - 1])
