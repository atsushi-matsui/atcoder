# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d

N = int(input())
S = input()

result = 0
for i in range(10**3):
    num3 = str(i).zfill(3)
    num3[0]
    num3[1]
    num3[2]

    r1 = S.find(num3[2])
    if r1 == -1:
        continue
    r2 = S.find(num3[1], r1 + 1)
    if r2 == -1:
        continue
    r3 = S.find(num3[0], r2 + 1)
    if r3 == -1:
        continue

    result += 1

print(result)
