# https://atcoder.jp/contests/abc249/tasks/abc249_c
import collections
import itertools


n, K = map(int, input().split())
L = []
for _ in range(n):
    L.append(input())

result = 0
for i in range(1, n + 1):
    # 組み合わせ ((0,1), (0,2)..)
    A = list(itertools.combinations(range(n), i))
    for j in A:
        c = collections.Counter()
        # (0,1)
        for k in j:
            # 0 next, 1
            for l in list(L[k]):
                c[l] += 1

        temp = 0
        for v in c.values():
            if v == K:
                temp += 1
        result = max(result, temp)

print(result)
