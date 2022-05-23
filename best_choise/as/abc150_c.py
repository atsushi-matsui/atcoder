# https://atcoder.jp/contests/abc150/tasks/abc150_c
import itertools

N = int(input())

P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

arr = []
for i in range(1, N + 1):
    arr.append(i)
R = list(itertools.permutations(arr))

for i, r in enumerate(R):
    if r == P:
        a = i + 1
    if r == Q:
        b = i + 1

print(abs(a - b))

"""
import copy

N = int(input())

p = list(input().split())
P = int("".join(p))
q = list(input().split())
Q = int("".join(q))

T = []
for i in range(N):
    T.append(i + 1)

count = 0
result = []


def dfs(n, t, r):
    global count
    if len(t) == 0:
        count += 1
        if r == P or r == Q:
            result.append(count)
    for i, tt in enumerate(t):
        t2 = copy.copy(t)
        t2.pop(i)
        dfs(n / 10, t2, r + n * tt)


for i, tt in enumerate(T):
    t2 = copy.copy(T)
    t2.pop(i)
    dfs(10 ** (N - 2), t2, 10 ** (N - 1) * tt)

if len(result) == 2:
    print(abs(result[0] - result[1]))
else:
    print(0)
"""
