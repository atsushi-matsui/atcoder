# https://atcoder.jp/contests/abc257/tasks/abc257_d
"""
訓練する回数(2分探索)
 始点(全探索)
  到達可能かの探索(BFS)
という考えで、最小の訓練回数を求める

O(logM*N^3) ※ Mは2分探索の右点
pypyじゃないとTLE
"""

from collections import deque

N = int(input())
X = []
Y = []
P = []
for _ in range(N):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)


def condition(Pi, S, xi, xj, yi, yj):
    return Pi * S >= abs(xi - xj) + abs(yi - yj)


def check(S):
    for i in range(N):
        visited = [False] * N
        q = deque()
        q.append(i)

        while len(q) > 0:
            s = q.popleft()

            if visited[s]:
                continue
            visited[s] = True

            for t in range(N):
                if s != t and condition(P[s], S, X[s], X[t], Y[s], Y[t]):
                    q.append(t)

        n = 0
        for v in visited:
            if v:
                n += 1
        if n == N:
            return True

    return False


left = -1
right = 10**18

while right - left > 1:
    middle = (right + left) // 2

    if check(middle):
        right = middle
    else:
        left = middle

print(right)
