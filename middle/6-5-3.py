# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c
N = int(input())
A = []
for _ in range(N):
   A.append(list(map(int, input().split())))

cost = []
ALL = 1 << N
for _ in range(ALL+1):
    cost.append([10**100]*N)

cost[0][0] = 0

#計算量：2^N*N^2
for i in range(ALL):
    for ni in range(N):
        for nj in range(N):
            # 訪問ずみの都市は無視
            if i & (1 << nj) > 0:
                continue
            # 同じ都市は無視
            if ni == nj:
                continue
            cost[i|1<<nj][nj] = min(cost[i|1<<nj][nj] ,cost[i][ni] + A[ni][nj])


# 全都市を訪問して開始点に戻る場合の最小コスト
print(cost[ALL-1][0])
