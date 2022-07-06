X, A, D, N = map(int, input().split())


def check(t):
    x1 = A + (t - 1) * D
    if x1 >= X:
        return True
    else:
        return False


def check_minus(t):
    x1 = A + (t - 1) * D
    if x1 <= X:
        return True
    else:
        return False


if D > 0:
    if X < A:
        res = abs(A - X)
    elif X > A + (N - 1) * D:
        res = abs(X - (A + (N - 1) * D))
    else:
        left = 0
        right = N
        while right - left > 1:
            middle = (right + left) // 2
            if check(middle):
                right = middle
            else:
                left = middle
        a = abs(X - (A + (right - 1) * D))
        b = abs(X - (A + (left - 1) * D))
        res = min(a, b)
if D < 0:
    if X > A:
        res = abs(X - A)
    elif X < A + (N - 1) * D:
        res = abs((A + (N - 1) * D) - X)
    else:
        left = 0
        right = N
        while right - left > 1:
            middle = (right + left) // 2
            if check_minus(middle):
                right = middle
            else:
                left = middle
        a = abs(X - (A + (right - 1) * D))
        b = abs(X - (A + (left - 1) * D))
        res = min(a, b)

if D == 0:
    res = abs(X - A)

print(res)
