# https://atcoder.jp/contests/dp/tasks/dp_a
N = int(input())
h = list(map(int, input().split()))

cost = [0] * N
for i in range(1, N):
    if i == 1:
        cost[i] = abs(h[i] - h[i - 1]) + cost[i - 1]
    else:
        cost[i] = min(
            abs(h[i] - h[i - 1]) + cost[i - 1], abs(h[i] - h[i - 2]) + cost[i - 2]
        )

print(cost[N - 1])
