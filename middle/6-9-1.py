# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a
# 計算量：log2
#NOTICE：2分探索の練習問題

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

#インデックスの初期値
ok = N
ng = -1

while abs(ok-ng) > 1:
    pipot = (ok+ng)//2
    if A[pipot] >= K:
        ok = pipot
    else:
        ng = pipot

if ok == N :
    print(-1)
else:
    print(ok)

