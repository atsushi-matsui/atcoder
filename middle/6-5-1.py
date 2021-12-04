# https://atcoder.jp/contests/past201912-open/tasks/past201912_g

N = int(input())
A = []
for _ in range(N):
    A.append([0]*N)
for i in range(N-1):
    a_list = list(map(int, input().split()))
    for j in range(N-i-1):
       A[i][i+j+1] = a_list[j]

# 集合の定義
ALL = 1<<N

# 幸福度の全ての組み合わせ
happy = [0]*ALL

# 集合nに要素iが含まれるか判定
def has_bit(n, i):
    return (n&i > 0)

# 幸福度の計算
# 計算量：2^N * N^2
for n in range(ALL):
    for i in range(N):
        for j in range(i+1, N):
            if has_bit(n ,1<<i) and has_bit(n ,1<<j):
                happy[n] += A[i][j]

# 結果を初期化
result = -10**100

# 計算量：4^N
for i in range(ALL):
    happy_one = happy[i]
    for j in range(ALL):
        if i&j > 0:
            continue
        happy_second = happy[j]
        happy_third = happy[(ALL-1)-(i|j)]
        
        result = max(result, happy_one+happy_second+happy_third)

print(result)