# import sys
#
# sys.setrecursionlimit(10**5)
#
N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))


P = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
ans = 0
for i in range(N):
    for j in range(N):
        for p, q in P:
            x, y = i, j
            now = 0
            for _ in range(N):
                now *= 10
                now += int(A[x][y])
                x += p
                y += q
                x %= N
                y %= N
            ans = max(ans, now)

print(ans)
