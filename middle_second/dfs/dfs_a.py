#https://atcoder.jp/contests/atc001/tasks/dfs_a
import sys
sys.setrecursionlimit(1000000)

H, W = list(map(int, input().split()))
grid = []
for _ in range(H):
    grid.append(input())

#スタートとゴール位置
sy = 0
sx = 0
gy = 0
gx = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == 's':
            sy, sx = i, j
        if grid[i][j] == 'g':
            gy, gx = i, j

#訪問済みであるのか
visited = []
for _ in range(H):
    visited.append([False]*W)

def dfs(i, j):
    visited[i][j] = True
    #ゴールしたなら処理終了
    #if i==gy and j==gx:
        #return
    for i2, j2 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        #区画内であるのか
        if not(0<=i2<H and 0<=j2<W):
            continue
        #壁は通行不可
        if grid[i2][j2] == '#':
            continue
        #訪問済みであるか
        if not visited[i2][j2]:
            dfs(i2, j2)        

dfs(sy, sx)

if visited[gy][gx]:
    print("Yes")
else:
    print("No")
