# https://atcoder.jp/contests/abc145/tasks/abc145_c
import copy

N = int(input())
XY = []
for _ in range(N):
    XY.append(list(map(int, input().split())))

results = []


def dfs(x, y, xy, r):

    if len(xy) == 0:
        results.append(r)
        return
    for i, cxy in enumerate(xy):
        cx = cxy[0]
        cy = cxy[1]
        d = ((cx - x) ** 2 + (cy - y) ** 2) ** (0.5)
        xy2 = copy.copy(xy)
        xy2.pop(i)
        dfs(cx, cy, xy2, r + d)


for i, xy in enumerate(XY):
    x = xy[0]
    y = xy[1]
    XYC = copy.copy(XY)
    XYC.pop(i)
    dfs(x, y, XYC, 0)

print(sum(results) / len(results))
