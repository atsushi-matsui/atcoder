INF = 2 * 10**5

N = int(input())
RL = []
for _ in range(N):
    r, l = map(int, input().split())
    RL.append((r, 1))
    RL.append((l, 2))

RL.sort(key=lambda x: (x[0], x[1]))

c = 0
r, l = 0, 0
res_r = []
res_l = []
for t, s in RL:
    if s == 1:
        c += 1
        if c == 1:
            res_r.append(t)

    if s == 2:
        c -= 1
        if c == 0:
            l = t
            res_l.append(t)

for i in range(len(res_r)):
    print(res_r[i], res_l[i])
