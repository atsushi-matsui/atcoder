# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d
import sys

sys.setrecursionlimit(2 * 10**6)

m = int(input())
n = int(input())

MN = []
for _ in range(n):
    MN.append(list(map(int, input().split())))

result = 0


def is_ok(nx, ny):
    if 0 <= nx < m and 0 <= ny < n:
        if is_passed[ny][nx]:
            return False
        if MN[ny][nx] == 1:
            return True

    return False


def dfs(x, y, count):
    global result
    is_passed[y][x] = True
    count += 1
    result = max(result, count)

    if is_ok(x - 1, y):
        dfs(x - 1, y, count)
    if is_ok(x, y - 1):
        dfs(x, y - 1, count)
    if is_ok(x + 1, y):
        dfs(x + 1, y, count)
    if is_ok(x, y + 1):
        dfs(x, y + 1, count)
    # 当該のルートで探索が完了したら、探索フラグを元に戻す
    is_passed[y][x] = False


is_passed = []
for i in range(n):
    for j in range(m):
        if MN[j][i] == 1:
            is_passed = [[False] * m for _ in range(n)]
            dfs(i, j, 0)

print(result)
