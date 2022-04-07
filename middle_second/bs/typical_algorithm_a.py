# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

left = -1
right = N

while abs(right - left) > 1:
    center = (right + left) // 2
    if A[center] > K:
        right = center
    else:
        left = center

if right == N:
    print(-1)
else:
    print(right)
