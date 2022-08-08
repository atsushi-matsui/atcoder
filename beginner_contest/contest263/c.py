import itertools

n ,m = map(int, input().split())

R = list(itertools.combinations(range(m), n))

for r in R:
    res = []
    for i in range(len(r)):
        res.append(str(int(r[i]) + 1))
    print(' '.join(res)) 