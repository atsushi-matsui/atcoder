# https://atcoder.jp/contests/abc128/tasks/abc128_c
# 計算量：O(2^N*PN)
N, M = map(int, input().split())
S = [0] * M
for i in range(M):
    s = list(map(int, input().split()))
    for j in range(1, s[0] + 1):
        S[i] = S[i] | 1 << (s[j] - 1)
P = list(map(int, input().split()))

result = 0
for n in range(1 << N):
    is_ok = True
    for i, p in enumerate(P):
        t = n & S[i]
        r = 0
        for j in range(N):
            if t >> j & 1 > 0:
                r += 1
        if r % 2 != p:
            is_ok = False
    if is_ok:
        result += 1

print(result)
