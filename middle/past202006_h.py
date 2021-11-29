# https://atcoder.jp/contests/past202004-open/tasks/past202004_h
N, M = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(input())

group = []
for _ in range(11):
    group.append([])

for i in range(N):
    for j in range(M):
        if A[i][j] == 'S':
            n = 0
        elif A[i][j] == 'G':
            n = 10
        else:
            n = int(A[i][j])
        group[n].append([i ,j])

# cost[i][j]:(i,j)にたどり着くまで最小移動回数の総和
cost = []
INF = 10**3
for i in range(N):
    cost.append([INF]*M)

# 初期条件
si, sj = group[0][0]
cost[si][sj] = 0

for n in range(1, 11):
    for i, j in group[n]:
        for i2, j2 in group[n-1]:
            cost[i][j] = min(cost[i][j], cost[i2][j2]+abs(i-i2)+abs(j-j2))

gi, gj = group[10][0]
if cost[gi][gj] ==  INF: 
    print(-1)
else:
    print(cost[gi][gj])