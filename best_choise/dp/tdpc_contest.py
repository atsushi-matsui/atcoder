# https://atcoder.jp/contests/tdpc/tasks/tdpc_contest
from unittest import result


N = int(input())
ps = [0] + list(map(int, input().split()))

p = sum(ps) + 1

conbine = []
for i in range(N + 1):
    conbine.append([False] * p)

# 初期値
conbine[0][0] = True

for i in range(1, N + 1):
    for j in range(p):
        # 解かなかった場合
        if conbine[i - 1][j]:
            conbine[i][j] = True
        # 解いた場合
        if j >= ps[i] and conbine[i - 1][j - ps[i]]:
            conbine[i][j] = True

result = 0
for con in conbine[N]:
    if con:
        result += 1

print(result)
