# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d
m = int(input())
M = []
for _ in range(m):
    x, y = map(int, input().split())
    M.append((x, y))

n = int(input())
N = []
for _ in range(n):
    x, y = map(int, input().split())
    N.append((x, y))


# 先頭を差分の起点にする
sx, sy = M[0]

delta_x = 0
delta_y = 0
for nx, ny in N:
    delta_x = nx - sx
    delta_y = ny - sy
    is_ok = True
    for mx, my in M:
        if not (mx + delta_x, my + delta_y) in N:
            is_ok = False
    if is_ok:
        break

print(delta_x, delta_y)
