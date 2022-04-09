# https://atcoder.jp/contests/abc077/tasks/arc084_a
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

result = 0

for n in range(N):
    left = -1
    right = N
    # NOTICE bisect.bisect_leftと同じ
    while abs(right - left) > 1:
        middle = (right + left) // 2
        if B[n] <= A[middle]:
            right = middle
        else:
            left = middle
    a = right
    # print("a", left, right)

    left = -1
    right = N
    # NOTICE bisect.bisect_rightと同じ
    while abs(right - left) > 1:
        middle = (right + left) // 2
        if B[n] >= C[middle]:
            left = middle
        else:
            right = middle
    c = N - right
    # print("c", left, right)

    result += a * c

print(result)
