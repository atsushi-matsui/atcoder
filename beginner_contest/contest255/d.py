# https://atcoder.jp/contests/abc255/tasks/abc255_d
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
X = []
for _ in range(Q):
    X.append(int(input()))

# 累積和を先に計算しといてあげる
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

for x in X:

    left = -1
    right = N

    while right - left > 1:
        middle = (right + left) // 2

        if x < A[middle]:
            right = middle
        else:
            left = middle

    a = right * x - S[right]
    b = S[N] - S[right] - (N - right) * x
    print(a + b)
