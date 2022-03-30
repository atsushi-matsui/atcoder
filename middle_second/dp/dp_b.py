# https://atcoder.jp/contests/dp/tasks/dp_b
# 実行環境はpypy3
N, K = map(int, input().split())
h = list(map(int, input().split()))

cost = [10**9] * (10**5 + 1)

# 初期値
cost[0] = 0

for i in range(1, N):
    for j in range(1, K + 1):
        if i - j >= 0:
            cost[i] = min(cost[i], cost[i - j] + abs(h[i] - h[i - j]))

print(cost[N - 1])
