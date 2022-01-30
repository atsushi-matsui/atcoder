#https://atcoder.jp/contests/abc007/tasks/abc007_3
from collections import deque

R, C = list(map(int,input().split()))
sy, sx = list(map(int,input().split()))
gy, gx = list(map(int,input().split()))
S = []
for i in range(R):
    S.append(input())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

dist = []
for i in range(R):
    dist.append([-1]*C)

Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

while len(Q) > 0:
    i, j = Q.popleft()
    
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        #枠の外の場合
        if not (0 <= i2 < R or 0 <= j2 < C):
            continue
        #壁の場合
        if S[i2][j2] == '#':
            continue
        #訪問済みの場合
        if dist[i2][j2] != -1:
            continue
        
        dist[i2][j2] = dist[i][j] + 1
        Q.append([i2, j2])
        # ゴールまでの距離を求めたら処理を終了
        if i2 == gy and j2 == gx:
            break

print(dist[gy][gx])