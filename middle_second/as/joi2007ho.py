# https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c
"""
2点が既知の場合の正方形の残りの点
q = (xj − yj + yi, yj + xj − xi)
r = (xi − yj + yi, yi + xj − xi)
"""
N = int(input())
MAX_XY = 5000
MIN_XY = 0
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
XY_HASH = set(XY)

"""
これで2分探索してもうまくいかない。。
def tp(x, y):
    l = -1
    r = N

    while r - l > 1:
        m = (r + l) // 2
        mx, my = XY[m]
        if x >= mx and y >= my:
            l = m
        else:
            r = m
    ax, ay = XY[l]
    return ax, ay
"""
result = 0
# この解法だと制限の3secギリギリでACになる
for i in range(N):
    xi, yi = XY[i]
    for j in range(i + 1, N):
        xj, yj = XY[j]
        qx, qy = xj - yj + yi, yj + xj - xi
        rx, ry = xi - yj + yi, yi + xj - xi
        if (
            MIN_XY <= qx <= MAX_XY
            and MIN_XY <= qy <= MAX_XY
            and MIN_XY <= rx <= MAX_XY
            and MIN_XY <= ry <= MAX_XY
        ):
            # in区で検索する際にlistだと遅すぎるのでHASH関数であるsetで検索する
            if (qx, qy) in XY_HASH and (rx, ry) in XY_HASH:
                result = max(result, (xi - xj) ** 2 + (yi - yj) ** 2)

"""
result = 0
XY.sort()
for xi, yi in XY:
    for xj, yj in XY:
        qx, qy = xj - yj + yi, yj + xj - xi
        rx, ry = xi - yj + yi, yi + xj - xi
        if (
            MIN_XY <= qx <= MAX_XY
            and MIN_XY <= qy <= MAX_XY
            and MIN_XY <= rx <= MAX_XY
            and MIN_XY <= ry <= MAX_XY
        ):
            sx, sy = tp(qx, qy)
            tx, ty = tp(rx, ry)
            if qx == sx and qy == sy and tx == rx and ty == ry:
                result = max(result, (xi - xj) ** 2 + (yi - yj) ** 2)
            
"""

print(result)
