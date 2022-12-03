# https://atcoder.jp/contests/abc265/tasks/abc265_c
"""
1.500 * 500 マスなので全探索で十分間に合う
2.同じマスを通った場合はループする
"""

H, W = map(int, input().split())
G = []
for h in range(H):
    G.append(list(input()))

def rec(T, i, j):
    if T[i][j] == 'U' and i != 0:
        return (i-1, j)
    elif T[i][j] == 'D' and i != H-1:
        return (i+1, j)
    elif T[i][j] == 'L' and j != 0:
        return (i, j-1)
    elif T[i][j] == 'R' and j != W-1:
        return (i, j+1)
    else:
        return (-1, -1)

V = [[False for _ in range(W)] for _ in range(H)]
ii, jj = 0, 0 
while 1:
   iii, jjj = rec(G, ii, jj)
   if (iii, jjj) == (-1, -1):
       print(ii+1, jj+1)
       break
   else:
       if not V[ii][jj]:
           V[ii][jj] = True
           ii, jj = iii, jjj
       else:
           print(-1)
           break
    

