#https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
sys.setrecursionlimit(1000000)

H, W = list(map(int, input().split()))
S = []
for i in range(H):
    S.append(input())

#ゴールの座標を設定
for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            si, sj = i, j
        if S[i][j] == "g":
            gi, gj = i, j

visited = []
for i in range(H):
    visited.append([False]*W)

def dfs(i, j):
    visited[i][j] = True

    for i2, j2 in [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]:
        if not (0 <= i2 < H and 0<= j2 < W):
            continue
        if S[i2][j2] == '#':
            continue
        if not visited[i2][j2]:
            dfs(i2, j2)

#始点から呼び出し
dfs(si, sj)

if visited[gi][gj]:
    print("Yse")
else:
    print("No")
    


