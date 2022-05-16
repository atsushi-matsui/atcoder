# https://atcoder.jp/contests/arc050/tasks/arc050_b
"""
補足
2≦x，y≦10^2　の制約と問題文から花束を作成するには少なくとも1本は赤も青も花が必要
花束をX個を作成するために赤X本、青X本を確保する
確保した以外の花を使って作成できる花束の合計をそれぞれ求める
 (R-X)/(x-1)と(B-X)/(y-1)
"""

R, B = list(map(int, input().split()))
x, y = list(map(int, input().split()))


def is_check(X):
    r = R - X
    b = B - X
    if r < 0 or b < 0:
        return False
    num = r // (x - 1) + b // (y - 1)
    return num >= X


left = 0
right = 10**18 + 1

while abs(left - right) > 1:
    center = (left + right) // 2
    if is_check(center):
        left = center
    else:
        right = center

print(left)
