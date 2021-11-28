#https://atcoder.jp/contests/dp/tasks/dp_a

import sys
sys.setrecursionlimit(10000000)

N = int(input())
h = list(map(int, input().split()))

cost = [0]*N
done = [False]*N

def rec(i):
    if done[i]:
        return cost[i]
        
    if i == 0:
        cost[i] = 0
    elif i == 1:
        cost[i] = abs(h[1]-h[0])
    else:
        cost[i] = min(rec(i-1)+abs(h[i]-h[i-1]), rec(i-2)+abs(h[i]-h[i-2]))

    done[i]=True
    return cost[i]

print(rec(N-1))