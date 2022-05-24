# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d

D, N = map(int, input().split())
T = []
for _ in range(D):
    T.append(int(input()))
A = []
B = []
C = []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

"""
i日目に服jを、i-1日目に服kを選んだ場合の派手さを
dp[i][j][k]
"""
dp = [[0] * N for _ in range(D + 1)]

for i in range(1, D):
    for j in range(N):
        for k in range(N):
            if A[k] <= T[i] <= B[k] and A[j] <= T[i - 1] <= B[j]:
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + abs(C[k] - C[j]))

print(max(dp[D]))
