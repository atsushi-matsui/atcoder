#https://atcoder.jp/contests/dp/tasks/dp_e
#FIXME 一部のテストでエラーとなるので要修正
N, W = list(map(int, input().split()))
V = 10**3

ws = [0]
vs = [0]
for i in range(N):
    w, v = list(map(int, input().split()))
    ws.append(w)
    vs.append(v)

weight = []
for i in range(N+1):
    weight.append([10**18]*(V+1))

weight[0][0] = 0

for i in range(1, N+1):
    for j in range(V+1):
        weight[i][j] = min(weight[i][j], weight[i-1][j])
        if j-vs[i] >= 0: 
            weight[i][j] = min(weight[i][j], weight[i-1][j-vs[i]]+ws[i])

max_value = 0
for i in range(1, V+1):
    if max_value < i and weight[N][i] <= W:
        max_value = i

print(max_value)