# https://atcoder.jp/contests/past202004-open/tasks/past202004_h
# NOTICE O(N^2M^2)となるが、N,M <= 50なので間に合う
N, M = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(input())

# 数字iの座標
point = []
for i in range(11):
    point.append([] * 50)
# 座標までの最短距離
dist = []
for i in range(N):
    dist.append([10**18] * M)

for i in range(N):
    for j in range(M):
        if A[i][j] != "S" and A[i][j] != "G":
            point[int(A[i][j])].append((i, j))
        if A[i][j] == "S":
            point[0].append((i, j))
        if A[i][j] == "G":
            point[10].append((i, j))

sx, sy, gx, gy = 0, 0, 0, 0

for i in range(N):
    for j in range(M):
        if A[i][j] == "S":
            sy, sx = i, j
        if A[i][j] == "G":
            gy, gx = i, j
# 初期化
dist[sy][sx] = 0

for i in range(1, 11):
    for y, x in point[i]:
        a = 0
        for yy, xx in point[i - 1]:
            dist[y][x] = min(dist[y][x], abs(y - yy) + abs(x - xx) + dist[yy][xx])

if dist[gy][gx] == 10**18:
    print(-1)
else:
    print(dist[gy][gx])
