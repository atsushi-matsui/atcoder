#https://atcoder.jp/contests/past202005-open/tasks/past202005_g
from collections import deque 

N, X, Y = list(map(int, input().split()))
base_x = 201
base_y = 201
X += base_x
Y += base_y

# ブロックマス
barrier = []
for _ in range(403):
    barrier.append([False]*403)
for _ in range(N):
    bx, by = list(map(int, input().split()))
    barrier[bx+base_x][by+base_y] = True

dist = []
for _ in range(403):
    dist.append([-1]*403)

Q = deque()
Q.append([base_x, base_y])
dist[base_x][base_y] = 0

while(len(Q) > 0):
    i, j = Q.popleft()

    if i == X and j == Y:
        break

    for i2, j2 in [[i+1, j+1], [i, j+1], [i-1, j+1], [i+1, j], [i-1, j], [i, j-1]]:
        #移動範囲
        if not(0 <= i2 <= 402 and 0 <= j2 <= 402):
            continue
        #壁マス
        if barrier[i2][j2]:
            continue
        #訪問済み
        if dist[i2][j2] != -1:
            continue

        dist[i2][j2] = dist[i][j] + 1
        Q.append([i2, j2])
        
print(dist[X][Y])