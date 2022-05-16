# https://atcoder.jp/contests/abc088/tasks/abc088_d
# 計算量：O(HW)

from collections import deque

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))

dot_count = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            dot_count += 1

d = []
for _ in range(H):
    d.append([-1] * W)

q = deque()
q.append((0, 0))
d[0][0] = 0

while len(q) > 0:
    y, x = q.popleft()

    if y == H - 1 and x == W - 1:
        break

    for y2, x2 in [(y, x - 1), (y + 1, x), (y, x + 1), (y - 1, x)]:
        if not (0 <= y2 < H and 0 <= x2 < W):
            continue
        if d[y2][x2] != -1:
            continue
        if S[y2][x2] == "#":
            continue

        d[y2][x2] = d[y][x] + 1
        q.append((y2, x2))

if d[H - 1][W - 1] == -1:
    print(-1)
else:
    print(dot_count - d[H - 1][W - 1] - 1)
