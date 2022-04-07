# https://atcoder.jp/contests/abc146/tasks/abc146_c
A, B, X = list(map(int, input().split()))
INT_MAX = 10**9
left = -1
right = INT_MAX + 1

while right - left > 1:
    N = (right + left) // 2
    cost = A * N + B * (len(str(N)))
    if cost > X:
        right = N
    else:
        left = N

if left == -1:
    print(0)
else:
    print(left)
