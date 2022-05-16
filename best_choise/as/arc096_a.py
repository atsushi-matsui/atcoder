# https://atcoder.jp/contests/abc095/tasks/arc096_a

A, B, C, X, Y = list(map(int, input().split()))

amount = 0
if A + B > C * 2:
    amount = C * 2 * min(X, Y)
    if X > Y:
        if A > 2 * C:
            amount += abs(X - Y) * 2 * C
        else:
            amount += abs(X - Y) * A
    else:
        if B > 2 * C:
            amount += abs(X - Y) * 2 * C
        else:
            amount += abs(X - Y) * B

else:
    amount = A * X + B * Y

print(amount)
