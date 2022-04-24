# https://atcoder.jp/contests/abc249/tasks/abc249_a
a, b, c, d, e, f, x = map(int, input().split())
ta, ao = 0, 0

xta = x
while xta > 0:

    if xta >= a:
        ta += a * b
        xta -= a
    else:
        ta += b * xta
        xta = 0
    xta -= c

xao = x
while xao > 0:
    if xao >= d:
        ao += d * e
        xao -= d
    else:
        ao += e * xao
        xao = 0
    xao -= f

if ta > ao:
    print("Takahashi")
if ta < ao:
    print("Aoki")
if ta == ao:
    print("Draw")
