# https://atcoder.jp/contests/dp/tasks/dp_d
N, W = map(int, input().split())

value = []
for _ in range(N+1):
    value.append([0]*(W+1))

for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(W+1):
        # 品物wを選ばなかった場合
        value[i][j] = max(value[i][j], value[i-1][j])
        # 品物wを選んだ場合
        if j >= w:
            value[i][j] = max(value[i][j], value[i-1][j-w]+v)

print(max(value[N]))