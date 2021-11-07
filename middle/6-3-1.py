#https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

#行数、列数
R, C  =list(map(int, input().split()))
#始点
sy, sx  =list(map(int, input().split()))
#終点
gy, gx  =list(map(int, input().split()))
#盤面
S = []
for i in range(R):
    S.append(input())

#配列用に座標を修正
sy -= 1
sx -= 1
gy -= 1
gx -= 1

#最小移動回数を管理する
dist = []
for i in range(R):
    dist.append([-1]*C)

#キューの設定（2次元座標）
Q = deque()
Q.append([sy, sx])

#始点
dist[sx][sy] = 0

#幅優先探索
while len(Q) > 0:
    i, j = Q.popleft()
    for i2, j2 in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
        if not(0 <= i2 < R and 0 <= j2< C):
            continue
        if S[i2][j2] == '#':
            continue
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])

print(dist[gy][gx])