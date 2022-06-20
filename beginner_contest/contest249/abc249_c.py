# https://atcoder.jp/contests/abc249/tasks/abc249_c
import collections

N, K = map(int, input().split())
L = [input() for _ in range(N)]

result = 0
"""
N=3の場合は以下の8通り。
0b000
0b001
0b010
0b011
0b100
0b101
0b110
0b111

0b011の場合は
L[1]とL[0]を選ぶ。
N-1=2 まで右にシフトして0b1との論理積が1の場合は対象である。
書き方は、(n >> i) & 1。nをiだけ右へビットシフトして1との論理積をとる
"""
for n in range(1 << N):
    c = collections.Counter()
    for i in range(N):
        if not (n >> i) & 1:
            continue
        for l in list(L[i]):
            c[l] += 1

        temp = 0
        for v in c.values():
            if v == K:
                temp += 1
        result = max(result, temp)

print(result)
