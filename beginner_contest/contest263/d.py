"""
lとrで置き換える場合を別々で考える。
まずはlから。

数列iまでの総和の最小値をL[i]とする。
- 一つ前までの最小値
L[i-1] + A[i]
- iまで全てlで置き換える場合
l*i
なので
L[i] = min(L[i-1] + A[i], l*i)
が総和の最小値。

同様にRも求める。


最後にL[i]+R[i+1]の最小値を求める
"""

n, l, r = map(int, input().split())
A = list(map(int, input().split()))

L = [0] * n
L[0] = min(A[0], l)
R = [0] * n
R[-1] = min(A[-1], r)

for i in range(0, n-1):
    L[i+1] = min(L[i] + A[i+1], l * (i+2))

for i in range(n-1, 0, -1):
    R[i - 1] += min(R[i] + A[i-1], r * (n-i+1))

res = 10**18
for i in range(-1, n):
    if i == -1:
        res = min(R[0], res)
    elif i == n-1:
        res = min(L[-1], res)
    else:
        res = min(L[i]+R[i+1], res)

print(res)