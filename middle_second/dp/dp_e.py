# https://atcoder.jp/contests/dp/tasks/dp_e
N, W = list(map(int, input().split()))
INF = 10**5+1
#重さ
weight = []
for _ in range(N+1):
    weight.append([10**10]*(INF))

#初期値
weight[0][0] = 0

for i in range(1, N+1):
    w, v = list(map(int, input().split()))
    for j in range(INF):
        weight[i][j] = min(weight[i][j], weight[i-1][j])
        if j >= v:
            weight[i][j] = min(weight[i][j], weight[i-1][j-v]+w)

result = 0
for v in range(INF):
    if weight[N][v] <= W:
        result = max(result, v)
    
print(result)