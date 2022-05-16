# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e

# これだとTLEになる
"""
R, C = map(int, input().split())
ROW = []
for _ in range(R):
    row = list(map(int, input().split()))
    r = 0
    for i, ro in enumerate(row):
        r += ro << i
    ROW.append(r)

result = 0
for i in range(1 << R):
    target_row = [0] * R
    for j in range(R):
        if (i >> j) & 1:
            target_row[j] = (1 << C) - ROW[j] - 1
        else:
            target_row[j] = ROW[j]

    res = 0
    for j in range(C):
        right_side = 0
        wrong_side = 0
        for k in range(R):
            if (target_row[k] >> j) & 1:
                right_side += 1
            else:
                wrong_side += 1
        res += max(right_side, wrong_side)

    result = max(result, res)


print(result)
"""

# pypy3環境だと通る
R, C = map(int, input().split())
RC = []
result = 0
for _ in range(R):
    RC.append(list(map(int, input().split())))

for i in range(1 << R):
    rows = [0] * C
    for j in range(R):
        if not ((i >> j) & 1):
            for k in range(C):
                rows[k] += (RC[j][k] + 1) % 2
        else:
            for k in range(C):
                rows[k] += RC[j][k]

    res = 0
    for row in rows:
        res += max(row, R - row)

    result = max(result, res)

print(result)
