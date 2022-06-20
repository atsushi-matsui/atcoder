# https://atcoder.jp/contests/abc249/tasks/abc249_a
a, b, c, d, e, f, x = map(int, input().split())


def culc(i, j, k):
    just = ((x // (i + k)) * i) * j
    re = min(x % (i + k), i) * j

    return just + re


ta = culc(a, b, c)
ao = culc(d, e, f)

if ta > ao:
    print("Takahashi")
if ta < ao:
    print("Aoki")
if ta == ao:
    print("Draw")
