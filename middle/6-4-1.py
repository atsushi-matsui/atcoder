#https://atcoder.jp/contests/dp/tasks/dp_a

N = int(input())
h = list(map(int, input().split()))

#初期値
cost = [0]*N
cost[0] = 0

#最初の足場
cost[1] = abs(h[1]-h[0])

#探索
for i in range(2,N):
    cost[i] = min(cost[i-1]+abs(h[i]-h[i-1]), cost[i-2]+abs(h[i]-h[i-2]))

print(cost[N-1])