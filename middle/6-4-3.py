# https://atcoder.jp/contests/dp/tasks/dp_d

N, W = list(map(int, input().split()))

ws = [0]
vs = [0]
for i in range(N):
    w, v = list(map(int, input().split()))
    ws.append(w)
    vs.append(v)

value = []
for i in range(N+1):
    value.append([-10**18]*(W+1))

#初期化
value[0][0] = 0

for i in range(1, N+1):
    for j in range(W+1):
        #品物iを使わない
        value[i][j] = max(value[i][j], value[i-1][j])
        #品物iを使う
        if j-ws[i] >= 0:
            value[i][j] = max(value[i][j], value[i-1][j-ws[i]]+vs[i])

ans = max(value[N])
print(ans)